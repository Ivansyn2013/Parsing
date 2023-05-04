# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class Jobparser(scrapy.Item):
    pass

class All4TatooIteam(scrapy.Item):
    name = scrapy.Field()
    diameter = scrapy.Field()
    fabric = scrapy.Field()
    thickness =scrapy.Field()
    _id = scrapy.Field()
class TryScrapyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
