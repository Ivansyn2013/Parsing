# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class LabirintBooksItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    link = scrapy.Field()
    authors = scrapy.Field()
    general_price = scrapy.Field()
    small_price = scrapy.Field()
    rate = scrapy.Field()
    img_ref = scrapy.Field()
    _id = scrapy.Field()