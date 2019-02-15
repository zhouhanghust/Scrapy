# -*- coding: utf-8 -*-
import scrapy


class ToScrapeSpiderXPath(scrapy.Spider):
    name = 'keywords-xpath'
    start_urls = []
    file_object = open('E:/code/KGQA_painter-master/quotesbot/quotesbot/data/txt/paints.txt', 'r', encoding="utf-8").readlines()

    for data in file_object:  #生成url列表
        start_urls.append(data.strip('\n').split(" ")[-1])
    print(start_urls)
    def parse(self, response):
        for quote in response.xpath('//div[@class="box1"]'):
            yield {
                'href': response.url,
                'keywords': quote.xpath('./h2/text()').extract_first(),
                'keydetail': quote.xpath('.//div[@class="scroll mCustomScrollbar"]//div[@class="text"]/p/text()').extract_first()
            }




