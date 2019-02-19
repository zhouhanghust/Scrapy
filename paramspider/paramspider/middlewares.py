# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
import random
import base64

class HeadersMiddleware(object):
    def __init__(self, crawler):
        super(HeadersMiddleware,self).__init__()
        self.my_headers = crawler.settings.get("MYDEFAULT_REQUEST_HEADERS", {}).items()
        self.ua = crawler.settings.get("MYUSER_AGENTS", [])

    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler)

    def process_request(self, request, spider):
        for k, v in self.my_headers:
            request.headers.setdefault(k, v)
        request.headers.setdefault('User-Agent', random.choice(self.ua))


# class ProxyMiddleware(object):
#     def __init__(self, crawler):
#         super(ProxyMiddleware,self).__init__()
#         self.proxy = crawler.settings.get("MYPROXIES", [])
#
#     @classmethod
#     def from_crawler(cls, crawler):
#         return cls(crawler)
#
#     def process_request(self, request, spider):
#         proxy = random.choice(self.proxy)
#         request.meta['proxy'] = "http://%s" % proxy['ip_port']
#         if proxy['user_pass'] is not None:
#             b64_data = base64.b64encode(proxy['user_pass'].encode()).strip()
#             # 设置账号密码认证                     认证方式   编码之后的账号密码
#             request.headers['Proxy-Authorization'] = 'Basic ' + b64_data.decode()
#             # 设置代理


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

