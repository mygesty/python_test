# -*- coding: utf-8 -*-
import scrapy
from ..items import DoutulaItem
from logging import getLogger
from  scrapy.log import msg

class DoutuSpider(scrapy.Spider):
    name = 'doutu'
    allowed_domains = ['www.doutula.com/']
    start_urls = ['http://www.doutula.com/article/list/?page=1']

    def parse(self, response):
        link = response.css('div.random_article div.col-xs-6.col-sm-3 img::attr(src)').extract()
        for link in link:
            item = DoutulaItem()
            item['link'] = link
            yield item
        msg('crawl all picture link,in all to 48')

