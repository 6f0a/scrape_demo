# settings.py

BOT_NAME = 'scrapy_demo'

SPIDER_MODULES = ['scrapy_demo.spiders']
NEWSPIDER_MODULE = 'scrapy_demo.spiders'

USER_AGENT =  'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36'

# FEED_URI = 'articles.json'
# FEED_FORMAT = 'json'

ROBOTSTXT_OBEY = False

DUPEFILTER_CLASS = 'scrapy.dupefilters.BaseDupeFilter'

ITEM_PIPELINES = {
   'nftscraping.pipelines.NftscrapingPipeline': 100,
   'nftscraping.pipelines.EndpointPipeline': 200
}

# Add Your ScrapeOps API Key
SCRAPEOPS_API_KEY = 'YOUR_API_KEY'

# Add In The ScrapeOps Extension
EXTENSIONS = {
        'scrapeops_scrapy.extension.ScrapeOpsMonitor': 500, 
        }

# Update The Download Middlewares
DOWNLOADER_MIDDLEWARES = {
'scrapeops_scrapy.middleware.retry.RetryMiddleware': 550,
'scrapy.downloadermiddlewares.retry.RetryMiddleware': None,
}


