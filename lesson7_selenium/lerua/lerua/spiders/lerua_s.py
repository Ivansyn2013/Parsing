import scrapy


class LeruaSSpider(scrapy.Spider):
    name = "lerua_s"
    allowed_domains = ["leroymerlin.ru"]
    start_urls = ["https://leroymerlin.ru/catalogue/arki-mezhkomnatnye/"]

    def parse(self, response):
        pass
