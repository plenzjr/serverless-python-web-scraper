import json
import scrapy
from scrapy.crawler import CrawlerProcess


class LululemonSpider(scrapy.Spider):
    name = "lululemon"
    start_urls = [
        "https://shop.lululemon.com/c/womens-leggings/_/N-8r6?format=json",
        "https://shop.lululemon.com/c/accessories/_/N-1z0xcmkZ1z0xl44Z8ok?format=json"
    ]

    def parse(self, response):
        data = json.loads(response.body)
        products = data['contents'][0]['mainContent'][0]['contents'][0]['records']
        for product in products:
            yield {
                'displayName': product['attributes']['product.displayName'][0],
                'category': product['attributes']['product.parentCategory.displayName'][0],
                'first_image': product['attributes']['product.sku.skuImages'][0],
                'price': product['attributes']['product.price'][0],
                'currency': product['attributes']['currencyCode'][0],
                'url': f"https://shop.lululemon.com/{product['attributes']['product.pdpURL'][0]}",
            }


def lambda_handler(event, context):

    output_path = "/tmp/items.json"
    process = CrawlerProcess(settings={
        "FEEDS": {
            output_path: {"format": "json"},
        },
    })
    process.crawl(LululemonSpider)
    process.start()
    try:
        with open(output_path, 'r') as f:
            items = json.load(f)
        print("Items loaded successfully")
        return {
            'statusCode': 200,
            'body': json.dumps(items)
        }
    except Exception as e:
        print(f"Error reading {output_path}: {e}")
        return {
            'statusCode': 500,
            'body': json.dumps({"message": "Internal server error"})
        }
