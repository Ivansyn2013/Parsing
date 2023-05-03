import scrapy
from scrapy.http import HtmlResponse
from twisted.internet import asyncioreactor
class MvideoSpider(scrapy.Spider):
    name = "mvideo"
    allowed_domains = ["mvideo.ru"]
    #асинхронно идет по ссылкам в списке и применяет методы
    start_urls = ["https://www.mvideo.ru/smartfony-i-svyaz-10/smartfony-205"]

    def parse(self, response: HtmlResponse):
        page_url = response.url
        print(page_url)

        yield page_url
