# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request, HtmlResponse
import os
import urllib.request

class MxSpider(scrapy.Spider):
    name = 'mx'
    allowed_domains = ['27270.com']
    start_urls = ['https://www.27270.com/ent/mingxingtuku/']

    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        'Host': 'www.27270.com',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36'
    }


    def make_requests_from_url(self, url):
        return Request(url, headers=self.headers, dont_filter=True)


    def parse(self, response):
        lst = response.css("body > div.warp.yh > div.MeinvTuPianBox > ul > li")

        header = {
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36',
            'Cookie':'Hm_lvt_bd92daaedea6aec43b7547409ba6f006=1550201109; Hm_lpvt_bd92daaedea6aec43b7547409ba6f006=1550215958'
        }

        for img in lst:
            name = img.css("a::attr(title)").extract_first()
            ImgUrl = img.css("a::attr(href)").extract_first()

            base_path = os.path.join("/Users/minlu/zhouhang/mingxingpic/",name)
            if not os.path.exists(base_path):
                os.makedirs(base_path)

            if ImgUrl is not None:
                yield response.follow(ImgUrl, meta={'base_path': base_path}, headers=header, callback=self.content)


        nextUrl = response.css("body > div.warp.yh > div.NewPages > ul > li > a::attr(href)")[-2].extract()
        nextName = response.css("body > div.warp.yh > div.NewPages > ul > li > a::text")[-2].extract()

        if nextName == '下一页':
            if nextUrl is not None:
                yield response.follow(nextUrl, callback=self.parse)


    def content(self,response):
        base_path = response.meta["base_path"]
        header = {
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36',
            'Cookie': 'Hm_lvt_bd92daaedea6aec43b7547409ba6f006=1550201109; Hm_lpvt_bd92daaedea6aec43b7547409ba6f006=1550215958'
        }

        imgurl = response.css("#picBody > p > a > img::attr(src)").extract_first()
        name = imgurl.split("/")[-1]
        file_path = os.path.join(base_path,name)

        if imgurl is not None:
            urllib.request.urlretrieve(imgurl, filename=file_path)

        nextUrl = response.css("li#nl > a::attr(href)").extract_first()
        if nextUrl != "##":
            yield response.follow(nextUrl, meta={'base_path': base_path}, headers=header, callback=self.content)






