# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from pymongo import MongoClient
from scrapy.pipelines.images import ImagesPipeline
from scrapy import Request

class LabirintBooksPipeline:
    def __init__(self):
        client = MongoClient("mongodb://root:example@0.0.0.0:22222/")
        self.mongo_db = client.mongo_db

    def process_item(self, item, spider):
        #collection = self.mongo_db[spider.name]
        #collection.insert_one(item)
        print(item)
        print('*'*10)
        print(spider)

        return item

class SaveImages(ImagesPipeline):
    def get_images(self, response, request, info, *, item=None):
        if item['img_ref']:
            try:
                yield Request(item['img_ref'][0])
            except Exception as error:
                print(error)
    def get_media_requests(self, item, info):
        if item['img_ref']:
            try:
                yield Request(item['img_ref'][0])
            except Exception as error:
                print(error)