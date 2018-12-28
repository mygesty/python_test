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
                        'spiderId=adb08076e78e44c8847b0fca36118ead&orderno=YZ201812113464RLejdX&' \
                        'returnType=2&count=5'
            for i in range(50):
                result = json.loads(requests.get(proxy_url).text).get('RESULT')
                for j in result:
                    proxies.append('http://' + j.get('ip') + ':' + j.get('port'))
                self.proxy = proxies
                self.add()

    def add(self):
        for i in self.proxy:
            self.db.sadd('proxy', i)

    def random(self):
        return self.db.srandmember('proxy').decode('utf-8')
