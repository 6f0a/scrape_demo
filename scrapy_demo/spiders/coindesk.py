import scrapy
import json
from scrapy.linkextractors import LinkExtractor
from scrapy_demo.items import NftscrapingItem
import datetime

article_list = ['bored ape yacht club','doodles','azuki','moonbirds']
url = 'https://api.queryly.com/json.aspx?queryly_key=d0ab87fd70264c0a&query={}&batchsize=10&showfaceted=true&extendeddatafields=basic,creator,creator_slug,subheadlines,primary_section,report_url,section_path,sections_paths,subtype,type,imageresizer,section,sponsored_label,sponsored,promo_image,pubDate&timezoneoffset=-120'

class CoindeskSpider(scrapy.Spider):
    name = 'coindesk'
    allowed_domains = ['www.coindesk.com','www.api.queryly.com']

    def start_requests(self):
        for collection in article_list:
            yield scrapy.Request(url.format(collection),cb_kwargs={'collection':collection})

    def parse(self, response,collection):
        article = NftscrapingItem()
        jsonresponse = response.json()['items']
        for item in jsonresponse:
            article['title'] = item['title']
            article['url'] = 'www.coindesk.com'+ item['link']
            article['datetime_crawled'] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            article['collection'] = collection
            article['datetime_posted'] = item['pubdate']
            article['source'] = 'CoinDesk'
            yield article