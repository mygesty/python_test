# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
# from selenium.webdriver import PhantomJS
from selenium.webdriver import Chrome
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
import time
from scrapy.http import HtmlResponse


class DoutulaDownloaderMiddleware(object):
    # @classmethod
    # def from_crawler(cls, crawler):
    #     # This method is used by Scrapy to create your spiders.
    #     s = cls()
    #     crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
    #     return s

    def __init__(self, timeout=10):
        # self.browser = PhantomJS()
        self.browser = Chrome()
        self.timeout = timeout
        self.wait = WebDriverWait(self.browser, self.timeout)

    def process_request(self, request, spider):
        self.browser.get(request.url)
        self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'span.page-link')))
        self.browser.execute_script('document.getElementsByClassName("page-link").scrollIntoView(True)')
        time.sleep(5)

        return HtmlResponse(url=request.url, body=self.browser.page_source, request=request,
                            status=200, encoding='utf-8')

    def __del__(self):
        self.browser.close()

    # def process_response(self, request, response, spider):
    #
    #     return response

    # def process_exception(self, request, exception, spider):
    #     # Called when a download handler or a process_request()
    #     # (from other downloader middleware) raises an exception.
    #
    #     # Must either:
    #     # - return None: continue processing this exception
    #     # - return a Response object: stops process_exception() chain
    #     # - return a Request object: stops process_exception() chain
    #     pass

    # def spider_opened(self, spider):
    #     spider.logger.info('Spider opened: %s' % spider.name)
