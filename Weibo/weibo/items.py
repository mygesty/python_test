# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class UserItem(scrapy.Item):
    collection = 'messege'
    follow_count = scrapy.Field()
    fans_count = scrapy.Field()
    statuses_count = scrapy.Field()
    verified = scrapy.Field()
    screen_name = scrapy.Field()
    id = scrapy.Field()

class FanItem(scrapy.Item):
    fan_id = scrapy.Field()
