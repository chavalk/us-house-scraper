import scrapy


class UshousespiderSpider(scrapy.Spider):
    name = "ushousespider"
    allowed_domains = ["live.house.gov"]
    start_urls = ["https://live.house.gov"]

    def parse(self, response):
        pass
