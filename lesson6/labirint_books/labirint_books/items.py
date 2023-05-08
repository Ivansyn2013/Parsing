# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from itemloaders.processors import MapCompose, Compose, TakeFirst

class LabirintBooksItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    link = scrapy.Field()
    authors = scrapy.Field(output_processor=TakeFirst())
    general_price = scrapy.Field()
    small_price = scrapy.Field()
    rate = scrapy.Field()
    img_ref = scrapy.Field(output_processor=TakeFirst())
    _id = scrapy.Field()
