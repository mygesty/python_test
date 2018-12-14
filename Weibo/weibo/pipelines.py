# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo


class MongoPipeline(object):
    def __init__(self, mongo_url, mongo_port, mongo_db):
        self.mongo_url = mongo_url
        self.mongo_port = mongo_port
        self.mongo_db = mongo_db

    @classmethod
    def from_crawl(cls, crawler):
        return cls(mongo_url=crawler.setting.MONGO_HOST, mongo_port=crawler.setting.MONGO_PROT,
                   mongo_db=crawler.setting.MONGO_DB)

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(host=self.mongo_url, port=self.mongo_port)
        self.db = self.client[self.mongo_db]

    def process_item(self, item, spider):
        self.db[item.collection].insert(dict(item))

    def close_spider(self, spider):
        self.client.close()
