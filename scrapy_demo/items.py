# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class NftscrapingItem(scrapy.Item):
    title = scrapy.Field()
    url = scrapy.Field()
    datetime_crawled = scrapy.Field()
    collection = scrapy.Field()
    datetime_posted = scrapy.Field()
    
