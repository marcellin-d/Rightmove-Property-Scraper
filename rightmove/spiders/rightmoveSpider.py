from rightmove.items import RightmoveItem
import scrapy
import json

class RightmoveSpider(scrapy.Spider):
    name = "rightmoveSpider"
    allowed_domains = ["www.rightmove.co.uk"]
    start_urls = ["https://www.rightmove.co.uk/house-prices/london-87490.html?pageNumber=1"]

    def parse(self, response):
        """
        Extracts property data from the page and yields it as a dictionary.
        Handles pagination to scrape multiple pages.
        """
        # Extraire le script contenant les données
        script_data = response.xpath('//script[contains(text(), "window.PAGE_MODEL")]/text()').get()

        if not script_data:
            self.logger.error("Script data not found on the page.")
            return

        # Extraire et parser le JSON
        try:
            start_index = script_data.find("window.PAGE_MODEL = ") + len("window.PAGE_MODEL = ")
            end_index = script_data.find("};", start_index) + 1
            json_str = script_data[start_index:end_index]
            data_json = json.loads(json_str)
        except (ValueError, TypeError):
            self.logger.error("Failed to parse JSON data.")
            return

        # Extraire les propriétés
        properties = data_json.get('searchResult', {}).get('properties', [])
        if not properties:
            self.logger.info("No properties found on this page.")
            return

        for property in properties:
            location = property.get('location', {})
            # Créer une instance de l'Item
            item = RightmoveItem()
            item['address'] = property.get('address')
            item['propertyType'] = property.get('propertyType')
            item['bedrooms'] = property.get('bedrooms')
            item['transactions'] = property.get('transactions', [])
            item['lat'] = location.get('lat')
            item['lon'] = location.get('lng')
            item['detailsUrl'] = property.get('detailUrl')
            
            yield item

        # Gestion de la pagination:

        # Recupere le numéro de page actuel en extrayant le dernier élément de l'URL
        current_page = int(response.url.split('=')[-1])

        # Calcul du numéro de page suivant
        next_page = current_page + 1
        
        # # Arrêter après la 5ème page
        if next_page > 3:
            self.logger.info("Reached page limit. Stopping pagination.")
            return

        # Construction de l'URL de la page suivante
        next_page_url = f"https://www.rightmove.co.uk/house-prices/london-87490.html?pageNumber={next_page}"

        # Si des propriétés sont trouvées sur la page actuelle, 
        # continuer à la page suivante en appelant la méthode parse() 
        # avec l'URL de la page suivante
        if properties:  
            self.logger.info(f"Scraping next page: {next_page_url}")
            yield response.follow(next_page_url, callback=self.parse)
