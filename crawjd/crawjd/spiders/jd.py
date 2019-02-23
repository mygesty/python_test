# -*- coding: utf-8 -*-
import scrapy
from crawjd.items import CrawjdItem
from urllib.parse import urlencode
from scrapy.loader import ItemLoader


class JdSpider(scrapy.Spider):
    name = 'jd'
    allowed_domains = ['www.jd.com','search.jd.com']

    def start_requests(self):
        dict = {}
        for keyword in self.settings.get('KEYWORD'):
            dict.update(keyword=keyword)
            for page in range(1,self.settings.get('CRAWL_PAGE')+1):
                page = page*2
                dict.update(page=page)
                url = 'https://search.jd.com/Search?' + urlencode(dict)
                yield scrapy.Request(url=url, callback=self.parse, dont_filter=True)

    def parse(self, response):
        result = response.xpath('//li[contains(@class,"gl-item")]')
        # for i in result:
        #     item = CrawjdItem()
        #     item['price'] = i.xpath('.//div[@class="p-price"]//strong/i/text()').extract_first()
        #     item['com_count'] = i.xpath('.//div[@class="p-commit"]//strong/a/text()').extract_first()
        #     item['brand'] = i.xpath('.//div[contains(@class,"p-name")]//em/text()[1]').extract_first()
        #     item['link'] = i.xpath('.//div[contains(@class,"p-name")]//href/text()').extract_first()
        #     yield item
        for selector in result:
            l = ItemLoader(item=CrawjdItem(), selector=selector)
            l.add_xpath('price', './/div[@class="p-price"]//strong/i/text()')
            l.add_xpath('com_count', './/div[@class="p-commit"]//strong/a/text()')
            l.add_xpath('brand', './/div[contains(@class,"p-name")]//em/text()[1]')
            l.add_xpath('link', './/div[contains(@class,"p-name")]//href/text()')
            yield l.load_item()
