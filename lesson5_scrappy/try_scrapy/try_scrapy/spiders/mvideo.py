import scrapy
from scrapy.http import HtmlResponse

class MvideoSpider(scrapy.Spider):
    name = "mvideo"
    allowed_domains = ["mvideo.ru"]
    start_urls = ["https://www.mvideo.ru/smartfony-i-svyaz-10/smartfony-205"]

    def parse(self, response: HtmlResponse):
        page_url = response.url
        print(page_url)

        return None
