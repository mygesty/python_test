# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
from pymongo.errors import DuplicateKeyError
from logging import getLogger


class MongoPipeline(object):
    def __init__(self, mongo_url, mongo_port, mongo_db):
        self.mongo_url = mongo_url
        self.mongo_port = mongo_port
        self.mongo_db = mongo_db
        self.logger = getLogger(__name__)

    @classmethod
    def from_crawler(cls, crawler):
        return cls(mongo_url=crawler.settings.get('MONGO_HOST'), mongo_port=crawler.settings.get('MONGO_PORT'),
                   mongo_db=crawler.settings.get('MONGO_DB'))

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(host=self.mongo_url, port=self.mongo_port)
        self.db = self.client[self.mongo_db]

    def process_item(self, item, spider):
        try:
            self.db[item.collection].insert(dict(item))
        except DuplicateKeyError:
            num = 1
            self.logger.warning('found {number} duplicatekeyerror'.format(number=num))
            num += 1
        finally:
            pass

    def close_spider(self, spider):
        self.client.close()
