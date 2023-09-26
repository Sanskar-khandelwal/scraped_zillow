import scrapy


class ZillowHousesSpider(scrapy.Spider):
    name = "zillow_houses"
    allowed_domains = ["zillow.com"]
    start_urls = ["https://zillow.com"]

    def parse(self, response):
        pass
