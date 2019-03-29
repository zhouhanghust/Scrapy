# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
from Pornpic2.items import Pornpic2Item
import os
import urllib.request
import re

class MeiziSpider(scrapy.Spider):
    name = 'meizi'
    allowed_domains = ['mzitu.com']
    start_urls = ['https://www.mzitu.com/xinggan/']

    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'if-modified-since': 'Thu, 14 Feb 2019 14:49:17 GMT',
        ':authority': 'www.mzitu.com',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
    }


    def make_requests_from_url(self, url):
        return Request(url, headers=self.headers, dont_filter=True)


    def parse(self, response):
        lst = response.css('#pins li')
        header = {
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
            'Cookie':'Hm_lvt_dbc355aef238b6c32b43eacbbf161c3c=1550155412,1550155414,1550155544; Hm_lpvt_dbc355aef238b6c32b43eacbbf161c3c=1550235125'
        }
        for img in lst:
            imgname = img.css("a img::attr(alt)").extract_first()
            imgname = re.sub(r' ', '', imgname)
            imgurl = img.css("a::attr(href)").extract_first()
            imgurl = str(imgurl)

            if imgurl is not None:
                yield scrapy.Request(imgurl, meta={'imgname': imgname}, headers=header, callback=self.content, dont_filter=True)

        nexturl = response.css("body > div.main > div.main-content > div.postlist > nav > div > a.next.page-numbers::attr(href)").extract_first()
        if nexturl is not None:
            yield response.follow(nexturl, callback=self.parse, dont_filter=True)

    def content(self,response):
        header = {
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
            'Cookie':'Hm_lvt_dbc355aef238b6c32b43eacbbf161c3c=1550155412,1550155414,1550155544; Hm_lpvt_dbc355aef238b6c32b43eacbbf161c3c=1550235125'
        }

        ImgUrl = response.css("body > div.main > div.content > div.main-image > p > a > img::attr(src)").extract_first()

        item = Pornpic2Item()
        item['name'] = response.meta['imgname']
        item['ImgUrl'] = [ImgUrl]
        yield item

        next_url = response.css("body > div.main > div.content > div.pagenavi > a::attr(href)")[-1].extract()
        nextname = response.css("body > div.main > div.content > div.pagenavi > a span::text")[-1].extract()
        if nextname == '下一组»' :
            next_url = None
        if next_url is not None:
            yield response.follow(next_url, meta={'imgname': item['name']}, headers=header, callback=self.content, dont_filter=True)

