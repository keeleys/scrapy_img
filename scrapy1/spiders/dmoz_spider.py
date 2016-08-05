import scrapy
from scrapy1.items import Scrapy1Item
class DmozSpider(scrapy.Spider):
    name = "v2ex"
    allowed_domains = ["v2ex.com"]
    start_urls = [
        "http://v2ex.com/"
    ]

    def parse(self, response):
        item = Scrapy1Item()
        for img in response.xpath('//img'):
            item['image_urls'] = img.xpath("@src").extract()
            yield item
