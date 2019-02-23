# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from scrapy.http import HtmlResponse


class CrawjdDownloaderMiddleware(object):
    def __init__(self,time_out=200):
        option = webdriver.ChromeOptions()
        option.add_argument("disable-infobars")
        self.time_out = time_out
        self.browser = webdriver.Chrome(options=option)
        self.wait = WebDriverWait(self.browser, self.time_out)

    def process_request(self, request, spider):
        # page = request.meta.get('page',1)
        try:
            self.browser.get(request.url)
            # if page > 1:
            #     input = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input#key")))
            #     submit = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button.button")))
            #     input.clear()
            #     input.send_keys("ipad")
            #     submit.click()
            self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input.input-txt")))
            self.browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
            time.sleep(1)
            return HtmlResponse(url=request.url, body=self.browser.page_source, request=request, encoding='utf-8', status=200)
        except TimeoutException:
            return HtmlResponse(url=request.url, status=500, request=request)

