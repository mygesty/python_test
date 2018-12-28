# -*- coding: utf-8 -*-
import scrapy
import time
import re
from ..items import ProxyItem


class ProxyCrawSpider(scrapy.Spider):
    name = 'proxy_craw'
    allowed_domains = ['www.xicidaili.com']
    craw_urls = ['http://www.xicidaili.com/nn/{page}']

    def start_requests(self):
        for i in range(1, 3501):
            yield scrapy.Request(self.craw_urls[0].format(page=i), callback=self.parse)

    def parse(self, response):
        result = response.css('tr')
        for i in result[1:]:
            item = ProxyItem()
            ip = i.xpath('td[2]/text()').extract_first()
            port = i.xpath('td[3]/text()').extract_first()
            http = i.xpath('td[6]/text()').extract_first()
            self.time = i.xpath('td[10]/text()').extract_first()
            self.epoch = i.xpath('td[9]/text()').extract_first()
            if self.time_parse():
                item['epoch'] = self.epoch
                item['proxy'] = list(map(lambda http, a, b: http.lower() + '://' + a + ':' + b, [http], [ip], [port]))[0]
                yield item

    # 解析并计算获取过期时间点
    def time_parse(self):
        ver_time = self.time.replace('-', ' ', 3).replace(':', ' ', 1)
        epoch = int(re.search('\d+', self.epoch).group())
        epoch_unit = re.search('\D+', self.epoch).group()  # 获取过期时间单位
        if epoch_unit == '分钟':
            epoch = epoch * 60
        elif epoch_unit == '小时':
            epoch = epoch * 3600
        else:
            epoch = epoch * 24 * 3600
        elasp = time.mktime(time.strptime(ver_time, '%y %m %d %H %M')) + epoch  # 获取过期时间点
        if elasp > time.time():  # 如果过期时间点超过现时间点则代理保存
            return True
        else:
            return False
