import scrapy
from scrapy.http import HtmlResponse
from twisted.internet import asyncioreactor
class MvideoSpider(scrapy.Spider):
    name = "mvideo"
    allowed_domains = ["mvideo.ru"]
    #асинхронно идет по ссылкам в списке и применяет методы
    #start_urls = ["https://www.mvideo.ru/smartfony-i-svyaz-10/smartfony-205"]
    # не работает сайт делает проверку на JS
    start_urls = ["https://lenta.ru/"]

    def parse(self, response: HtmlResponse):
        x_path_str = "//a[contains(@class,'card-mini')]/@href"
        smart_fones = response.xpath(x_path_str).getall()
        print(len(smart_fones))
        for link  in smart_fones:
            print('*'*10)
            print(link)
            yield response.follow(link, callback=self.parse_smartfone)

    def parse_smartfone(self, responce: HtmlResponse):
        x_path_str = "//span[contains(@class, 'topic-body__title')]"
        print('*'*10)
        print(responce.url)