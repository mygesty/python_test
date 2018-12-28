# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from pymongo import MongoClient


class ProxyPipeline(object):
    def __init__(self, host, port):
        self.host = host
        self.port = port

    @classmethod
    def from_crawler(cls, crawler):
        return cls(host=crawler.settings.get('MONGO_HOST'), port=crawler.settings.get('MONGO_PORT'))

    def open_spider(self, spider):
        self.client = MongoClient(host=self.host, port=self.port)
        self.db = self.client['proxy']
        self.collection = self.db['proxies']

    def process_item(self, item, spider):
        self.collection.insert_one(dict(item))
        return item

    def close_spider(self, spider):
        self.client.close()
