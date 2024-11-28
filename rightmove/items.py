import scrapy

class RightmoveItem(scrapy.Item):
    """
    Represents a property item scraped from Rightmove.
    
    Attributes:
        address (scrapy.Field): The address of the property.
        propertyType (scrapy.Field): The type of the property (e.g., house, flat).
        bedrooms (scrapy.Field): The number of bedrooms in the property.
        transactions (scrapy.Field): The transaction history of the property.
        lat (scrapy.Field): The latitude of the property's location.
        lon (scrapy.Field): The longitude of the property's location.
        detailsUrl (scrapy.Field): The URL to the property's detail page.
    """
    address = scrapy.Field()
    propertyType = scrapy.Field()
    bedrooms = scrapy.Field()
    transactions = scrapy.Field()
    lat = scrapy.Field()
    lon = scrapy.Field()
    detailsUrl = scrapy.Field()

