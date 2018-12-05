# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractor import LinkExtractor
from ..items import MatplotExampleItem


class MatplotSpider(scrapy.Spider):
    name = 'matplot'
    allowed_domains = ['matplotlib.org']
    start_urls = ['http://matplotlib.org/examples/index.html']

    def parse(self, response):
        link = LinkExtractor(restrict_css='div.toctree-wrapper.compound', deny='index.html$')
        for link in link.extract_links(response):
            yield scrapy.Request(url=link.url, callback=self.file_parse)

    def file_parse(self, response):
        item = MatplotExampleItem()
        href = response.css('a.reference.external::attr(href)').extract_first()
        url = response.urljoin(href)
        item['file_urls'] = [url]
        return item
