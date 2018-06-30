# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo

class GuaziPipeline(object):
    def open_spider(self,spider):
        self.client = pymongo.MongoClient("localhost",27017)
        self.guazi = self.client.guazi

    def process_item(self, item, spider):
        self.guazi.car.insert_one(dict(item))
        return item

    def close_spider(self, spider):
        self.client.close()
