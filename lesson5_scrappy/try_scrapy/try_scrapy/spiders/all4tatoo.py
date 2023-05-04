import scrapy
from scrapy.http import HtmlResponse

class All4tatooSpider(scrapy.Spider):
    name = "all4tatoo"
    allowed_domains = ["www.all4tattoo.ru"]
    start_urls = ["https://www.all4tattoo.ru/piercing/titanium/"]

    def parse(self, response: HtmlResponse):
        x_path_str = "//div[contains(@class,'thumbnail')]/a/@href"
        x_path_str_next = "//a[contains(text(),'Туда')]"
        next_page = response.xpath(x_path_str_next).get()
        if next_page:
            yield response.follow(next_page, callback=self.parse)

        jewels = response.xpath(x_path_str).getall()
        for link in jewels:
            print(link)
            yield response.follow(link, callback=self.parse_jevely)

    def parse_jevely(self, responce: HtmlResponse):
        print('*'*10)
        print(responce.url)