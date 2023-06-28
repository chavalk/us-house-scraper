import scrapy


class UshousespiderSpider(scrapy.Spider):
    name = "ushousespider"
    allowed_domains = ["liveproxy-azapp-prod-eastus2-003.azurewebsites.net"]
    start_urls = ["https://liveproxy-azapp-prod-eastus2-003.azurewebsites.net/latest/floor"]

    def parse(self, response):
        jsonresponse = response.json()

        yield {
            '_id' : jsonresponse.get('_id')
        }
