# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
import random
import base64
from fake_useragent import UserAgent
import json

class HeadersMiddleware(object):
    def __init__(self, crawler):
        super(HeadersMiddleware,self).__init__()
        self.my_headers = crawler.settings.get("MYDEFAULT_REQUEST_HEADERS", {}).items()
        # self.ua = crawler.settings.get("MYUSER_AGENTS", [])
        self.ua = UserAgent()
        self.ua_type = crawler.settings.get("RANDOM_UA_TYPE", "random")

    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler)

    def process_request(self, request, spider):
        for k, v in self.my_headers:
            request.headers.setdefault(k, v)
        # request.headers.setdefault('User-Agent', random.choice(self.ua))
        # request.headers.setdefault('User-Agent', self.ua.random)

        def get_ua():
            return getattr(self.ua, self.ua_type)

        request.headers.setdefault('User-Agent', get_ua())


class ProxyMiddleware(object):
    def __init__(self, crawler):
        super(ProxyMiddleware,self).__init__()
        # self.proxy = crawler.settings.get("MYPROXIES", [])
        with open("../tools/ips.json", "r", encoding="utf-8") as f:
            self.iplist = json.load(f)


    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler)

    def process_request(self, request, spider):
        proxy = random.choice(self.iplist)
        request.meta['proxy'] = proxy
        # 强制设置一个
        # request.meta['proxy'] = 'http://58.48.168.166:51430'
        # request.meta['proxy'] = "http://%s" % proxy['ip_port']
        # if proxy['user_pass'] is not None:
        #     b64_data = base64.b64encode(proxy['user_pass'].encode()).strip()
        #     # 设置账号密码认证                     认证方式   编码之后的账号密码
        #     request.headers['Proxy-Authorization'] = 'Basic ' + b64_data.decode()


class MyCookiesMiddleware(object):
    def __init__(self, crawler):
        super(MyCookiesMiddleware,self).__init__()
        self.cookies = crawler.settings.get("COOKIES", {}).items()

    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler)

    def process_request(self, request, spider):
        for k, v in self.cookies:
            request.cookies.setdefault(k, v)

