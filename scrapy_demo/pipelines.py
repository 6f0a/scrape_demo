# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import requests


class ScrapyDemoPipeline:
    def process_item(self, article, spider):
        return article

class EndpointPipeline:
    def process_item(self, article, spider):
        data = {
            'title': article['title'],
            'url': article['url'],
            'datetime_crawled': article['datetime_crawled'],
            'collection': article['collection'],
            'datetime_posted':article['datetime_posted']
        }
        headers = {'Content-Type': 'application/json'}
        r = requests.post('https://postman-echo.com/post', json=data, headers=headers)
        print(r.text)
        return article
