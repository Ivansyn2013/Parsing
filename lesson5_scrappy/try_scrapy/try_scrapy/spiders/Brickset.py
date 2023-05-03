import scrapy


class BricksetSpider(scrapy.Spider):
    name = "Brickset"
    allowed_domains = ["brickset.com"]
    start_urls = ["https://brickset.com/sets/theme-Avatar/year-2023"]

    def parse(self, response):
        pass
#scrapy runspider scraper.py