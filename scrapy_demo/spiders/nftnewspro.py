import scrapy
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor
from scrapy_demo.items import NftscrapingItem
from scrapy_demo.article_list import list
import datetime



article_list = list
url = 'https://nftnewspro.com/?s={}'

class NftnewsproSpider(scrapy.Spider):
    name = 'nftnewspro'
    allowed_domains = ['nftnewspro.com']

    def start_requests(self):
        for collection in article_list:
            yield scrapy.Request(url.format(collection),cb_kwargs={'collection':collection})
    
    def parse(self,response,collection):
        for link in response.xpath('//article/a[@class="post-thumbnail"]/@href')[:10]:
            yield response.follow(link.get(),callback = self.parse_item,cb_kwargs = {'collection':collection})

    def parse_item(self, response,collection):
        article = NftscrapingItem()
        title_selector = response.xpath('//title/text()')
        article['title'] = title_selector.get()
        article['url'] = response.url
        article['datetime_crawled'] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        article['collection'] = collection
        datetime_object = datetime.datetime.strptime(''.join(response.xpath('//meta[@property = "article:published_time"]/@content').extract()),'%Y-%m-%dT%H:%M:%S%z')
        article['datetime_posted'] = datetime_object.strftime("%Y-%m-%d %H:%M:%S")
        article['source'] = 'Nftnewspro'
        return article