# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exceptions import DropItem
from scrapy.item import Item
import pymongo
class MongoDBPipeline(object):
    DB_URL ='mongodb://localhost:27017'
    DB_NAME = 'scrapy_test'
    def open_spider(self,spider):
        self.client = pymongo.MongoClient(self.DB_URL)
        self.db = self.client[self.DB_NAME]

    def close_spider(self,spider):
        self.client.close()

    def process_item(self,item,spider):
        collection = self.db[spider.name]
        post = dict(item) if isinstance(item,Item) else item
        collection.insert_one(post)
        return  item

class PriceConverterPipeline(object):
    def __init__(self):
        self.exchange = 8.5309
    def process_item(self,item,spider):
        price = float(item['price'][1:])*self.exchange
        item['price'] = '￥%.3f'%price
        return item

class DuplicatesPipeline(object):
    def __init__(self):
        self.book_set = set()
    def process_item(self,item,spider):
        name = item['name']
        if name in self.book_set:
            raise DropItem('Duplicate book found:%s'%item)
        self.book_set.add(name)
        return item
