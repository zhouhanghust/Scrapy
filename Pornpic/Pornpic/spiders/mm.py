# -*- coding: utf-8 -*-
import scrapy
from Pornpic.items import PornpicItem

class MmSpider(scrapy.Spider):
    name = 'mm'
    allowed_domains = ['mm131.com']
    start_urls = ['http://www.mm131.com/xinggan/',
                  ]

    def parse(self, response):
        lst = response.css('body > div.main > dl > dd')
        for img in lst:
            imgname = img.css("a::text").extract_first()
            imgurl = img.css("a::attr(href)").extract_first()
            imgurl = str(imgurl)
            yield scrapy.Request(imgurl, callback=self.content, dont_filter=True)


        nexturl = response.css("body > div.main > dl > dd.page > a:nth-child(12)::attr(href)").extract_first()
        if nexturl is not None:
            yield response.follow(nexturl, callback=self.parse, dont_filter=True)

    def content(self,response):
        item = PornpicItem()
        item['name'] = response.css("body > div.content > h5::text").extract_first()
        item['ImgUrl'] = response.css("body > div.content > div.content-pic > a > img::attr(src)").extract()
        yield item

        next_url = response.css("body > div.content > div.content-page > a.page-ch::attr(href)").extract_first()
        if next_url is not None:
            yield response.follow(next_url, callback=self.content, dont_filter=True)