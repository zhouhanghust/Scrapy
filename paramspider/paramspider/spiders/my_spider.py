# -*- coding: utf-8 -*-
import scrapy


class MySpiderSpider(scrapy.Spider):
    name = 'my_spider'
    allowed_domains = ['httpbin.org']
    start_urls = ['http://httpbin.org/']


    def parse(self, response):
        print("request meta: %s" % response.request.meta)
        print("request headers: %s" % response.request.headers)
        print("request cookies: %s" % response.request.cookies)