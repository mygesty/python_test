# -*- coding: utf-8 -*-
import scrapy
from ..items import CatItem


class CatCrawlSpider(scrapy.Spider):
    name = 'cat_crawl'
    allowed_domains = ['placekitten.com/g/']
    base_url = 'http://placekitten.com/g/'
    start_urls = ['http://placekitten.com/g//']

    def parse(self, response):
        link = response.xpath('//pre/a/@href').re(r'(\d.*)/')
        url = []
        for i in link:
            i = self.base_url+i+'/'+i
            url.append(i)
        item = CatItem()
        item['image_urls'] = url
        yield item
