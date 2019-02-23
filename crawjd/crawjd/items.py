# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field


class CrawjdItem(Item):
    collection = 'products'
    price = Field()
    com_count = Field()
    brand = Field()
    link = Field()
    chip = Field()

