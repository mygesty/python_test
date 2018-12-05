# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

import logging


class ProxyMiddleware(object):
    logger = logging.getLogger(__name__)

    def process_request(self, request, spider):
        self.logger.debug('Trying using proxy')
        request.meta['proxy'] = 'http://218.87.170.17:8088'
        return None
