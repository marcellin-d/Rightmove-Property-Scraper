# Scrapy settings for rightmove project

BOT_NAME = "rightmove"

SPIDER_MODULES = ["rightmove.spiders"]
NEWSPIDER_MODULE = "rightmove.spiders"

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# DOWNLOAD_DELAY = 3

# Disable cookies (enabled by default)
# COOKIES_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-GB,en;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
}

# Enable or disable spider middlewares
# SPIDER_MIDDLEWARES = {
#     "rightmove.middlewares.RightmoveSpiderMiddleware": 543,
# }

# Enable or disable downloader middlewares
#DOWNLOADER_MIDDLEWARES = {
 #   'zyte_smart_proxy_middleware.SmartProxyMiddleware': 610,
    # Autres middlewares de Scrapy
#}

LOG_LEVEL = 'INFO'

# Configure item pipelines
ITEM_PIPELINES = {
    'rightmove.pipelines.MongoDBPipeline': 1,
}

# Set settings whose default value is deprecated to a future-proof value
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"

FEEDS = {
    'rightmove.csv': {
        'format': 'csv',
        'encoding': 'utf8',
        'store_empty': False,
        'fields': ['address', 'propertyType', 'bedrooms', 'transactions', 'lat', 'lon', 'detailsUrl'],
        'overwrite': True,
    },
}

# URI pour se connecter à MongoDB
MONGO_URI = 'mongodb://localhost:27017'

# Nom de la base de données
MONGO_DATABASE = 'scrapy_db'

# Nom de la collection
MONGO_COLLECTION = 'raw_properties'

# Activer l'utilisation des proxies Zyte
HTTP_PROXY = 'http://proxy.zyte.com:8010'
