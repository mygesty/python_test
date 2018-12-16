import requests
import json
from redis import StrictRedis


class RedisClient(object):
    def __init__(self):
        self.db = StrictRedis(host='114.116.123.62', port=6379, db=1)
        self.crawl_xundaili()

    def crawl_xundaili(self):
        if self.db.scard('proxy') == 0:
            proxies = []
            proxy_url = 'http://api.xdaili.cn/xdaili-api//greatRecharge/getGreatIp?' \
                        'spiderId=adb08076e78e44c8847b0fca36118ead&orderno=YZ201812110025' \
                        't1mlPQ&returnType=2&count=20'
            result = json.loads(requests.get(proxy_url).text).get('RESULT')
            for i in result:
                proxies.append('http://' + i.get('ip') + ':' + i.get('port'))
            self.proxy = proxies
            self.add()

    def add(self):
        for i in self.proxy:
            self.db.sadd('proxy', i)

    def random(self):
        return self.db.srandmember('proxy').decode('utf-8')
