import scrapy


class BricksetSpider(scrapy.Spider):
    name = "Brickset"
    allowed_domains = ["brickset.com"]
    start_urls = ["http://brickset.com/"]

    def parse(self, response):
        pass
