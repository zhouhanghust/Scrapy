# -*- coding: utf-8 -*-
import scrapy
from Xian.items import XianItem
import urllib.request

class XnSpider(scrapy.Spider):
    name = 'xn'
    allowed_domains = ['hi0590.com']
    start_urls = ['http://www.hi0590.com/']

    def parse(self, response):
        lst = response.css("body > div.main > div.pic > ul > li > a")
        for img in lst:
            imgname = img.css("img::attr(alt)").extract_first()
            imgurl = img.css("a::attr(href)").extract_first()

            if imgurl is not None:
                yield response.follow(imgurl, meta={'imgname':imgname}, callback=self.content)

        next_urls = response.css("body > div.main > div.pic > div > a.ch")
        nexturl = None
        for each in next_urls:
            if each.css("a::text").extract_first() == '下一页':
                nexturl = each.css("a::attr(href)").extract_first()

        if nexturl is not None:
            yield response.follow(nexturl, callback=self.parse)

    def content(self, response):
        item = XianItem()
        item['name'] = response.meta['imgname']
        item['ImgUrl'] = response.css("#content > a > img::attr(src)").extract()

        yield item

        if item['ImgUrl'] :
            tailis = item['ImgUrl'][0].split("/")[-1]
            file_path = "/Users/zhouxiaohang/PycharmProjects/ssass/{0}_{1}".format(item['name'], tailis)
            urllib.request.urlretrieve(item['ImgUrl'][0], filename=file_path)

        nextcontent = response.css("#page > a.ch.next")
        next_name = nextcontent.css("a::text").extract_first()
        next_url = nextcontent.css("a::attr(href)").extract_first()

        if next_name == '下一页':
            yield response.follow(next_url, meta={'imgname':item['name']}, callback=self.content)