import pymongo

class MongoDBPipeline:
    def __init__(self, mongo_uri, mongo_db, collection_name):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db
        self.collection_name = collection_name

    @classmethod
    def from_crawler(cls, crawler):
        """
        Méthode utilisée pour récupérer les paramètres depuis les settings.py.
        """
        return cls(
            mongo_uri=crawler.settings.get('MONGO_URI', 'mongodb://localhost:27017'),
            mongo_db=crawler.settings.get('MONGO_DATABASE', 'scrapy_db'),
            collection_name=crawler.settings.get('MONGO_COLLECTION', 'raw_properties')
        )

    def open_spider(self, spider):
        """
        Initialiser la connexion à MongoDB.
        """
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def close_spider(self, spider):
        """
        Fermer la connexion à MongoDB.
        """
        self.client.close()

    def process_item(self, item, spider):
        """
        Enregistrer chaque item dans la collection MongoDB.
        """
        self.db[self.collection_name].insert_one(dict(item))
        return item
