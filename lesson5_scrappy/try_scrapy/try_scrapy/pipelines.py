# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from pymongo import MongoClient


class TryScrapyPipeline:
    def __init__(self):
        client = MongoClient("mongodb://root:example@0.0.0.0:22222/")
        self.mongo_db = client.mongo_db
    def process_item(self, item, spider):
        collection = self.mongo_db[spider.name]
        collection.insert_one(item)
        #print(item)
        #print('*'*10)
        #print(spider)

        return item
