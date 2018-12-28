# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ProxyItem(scrapy.Item):
    proxy = scrapy.Field()
    epoch = scrapy.Field()
