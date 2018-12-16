# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
import json
from ..items import UserItem, FanItem


class WeiboCrawlSpider(scrapy.Spider):
    name = 'weibo_crawl'
    allowed_domains = ['m.weibo.cn']
    start_id = ['1662068793']
    user_url = 'https://m.weibo.cn/profile/info?uid={uid}'
    follows_url = 'https://m.weibo.cn/api/container/getIndex?containerid=231051_-_followers_-_{uid}&page={page}'
    fans_url = 'https://m.weibo.cn/api/container/getIndex?containerid=231051_-_fans_-_{uid}&since_id={page}'

    def start_requests(self):
        for i in self.start_id:
            yield Request(url=self.user_url.format(uid=i), callback=self.parse_user)

    def parse_user(self, response):
        useritem = UserItem()
        result = json.loads(response.text)
        result = result.get('data').get('user')
        user_info = {'id': 'id', 'follow_count': 'follow_count', 'fans_count': 'followers_count',
                     'statuses_count': 'statuses_count', 'verified': 'verified', 'screen_name': 'screen_name'}
        for key, value in user_info.items():
            useritem[key] = result.get(value)
        yield useritem
        _id = result.get('id')
        follow_page = result.get('follow_count') // 20
        fans_page = result.get('followers_count') // 20
        for i in range(fans_page):
            i += 1
            yield Request(url=self.fans_url.format(uid=id, page=i), callback=self.parse_fan)
        for i in range(follow_page):
            i += 1
            yield Request(url=self.follows_url.format(uid=id, page=i), callback=self.parse_follower)

    def parse_fan(self, response):
        result = json.loads(response.text)
        result = result.get('data').get('cards')[0].get('card_group')
        for i in result:
            id = i.get('user').get('id')
            yield Request(url=self.user_url.format(uid=id), callback=self.parse_user)

    def parse_follower(self, response):
        result = json.loads(response.text)
        result = result.get('data').get('cards')[0].get('card_group')
        for i in result:
            id = i.get('user').get('id')
            yield Request(url=self.user_url.format(uid=id), callback=self.parse_user)

