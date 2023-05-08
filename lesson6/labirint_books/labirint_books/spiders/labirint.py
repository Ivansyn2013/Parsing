import scrapy
from scrapy.http import HtmlResponse
from scrapy.loader import ItemLoader
from ..items import LabirintBooksItem
class LabirintSpider(scrapy.Spider):
    name = "labirint"
    allowed_domains = ["labirint.ru"]
    start_urls = ["https://www.labirint.ru/books/"]

    def parse(self, response: HtmlResponse):
        x_path_str = '//img[@class="book-img-cover"]/parent::a/@href'
        x_path_next_page = '//a[contains(@class,"pagination-next")]'

        next_page = response.xpath(x_path_next_page).get()
        if next_page:
            yield response.follow(next_page, callback=self.parse)

        books = response.xpath(x_path_str).getall()

        for index, book in enumerate(books):
            print(book)
            #ограничение парсинга
            if index > 2:
                break
            yield response.follow(book, callback=self.parse_book)


    def parse_book(self, responce: HtmlResponse):
        loader = ItemLoader(item=LabirintBooksItem(), response=responce)
        loader.add_value('link', responce.url)
        x_path_name = '//h1/text()'
        x_path_authors = '//div[@class="authors"]/text()'
        x_path_general_price = '//span[@class="buying-priceold-val-number"]/text()'
        x_path_small_price = '//span[@class="buying-pricenew-val-number"]/text()'
        x_path_rate = '//div[@id="rate"]/text()'
        x_path_img = '//img[@class="book-img-cover"]/@src'

        loader.add_xpath('name', x_path_name)
        loader.add_xpath('authors', x_path_authors)
        loader.add_xpath('general_price', x_path_general_price)
        loader.add_xpath('small_price', x_path_small_price)
        loader.add_xpath('rate', x_path_rate)
        loader.add_xpath('img_ref', x_path_img)

        print('8'*10)
        print(responce.url)
