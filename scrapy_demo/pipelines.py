# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import requests
import boto3
import json
from botocore.exceptions import ClientError

def get_secret():

    secret_name = "prod/OditoAPI/Admin"
    region_name = "eu-central-1"

    # Create a Secrets Manager client
    session = boto3.session.Session()
    client = session.client(
        service_name='secretsmanager',
        region_name=region_name
    )

    try:
        get_secret_value_response = client.get_secret_value(
            SecretId=secret_name
        )
    except ClientError as e:
        # For a list of exceptions thrown, see
        # https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_GetSecretValue.html
        raise e

     # Decrypts secret using the associated KMS key.
    secret = json.loads(get_secret_value_response['SecretString'])
    return secret['API_KEY_METAQUANTS']

    # Your code goes here.


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
        headers = {'Content-Type': 'application/json', 'x-api-key': get_secret()}
        r = requests.post('https://api.metaquants.xyz/v1/scraping', json=data, headers=headers)
        print(r.text)
        return article
