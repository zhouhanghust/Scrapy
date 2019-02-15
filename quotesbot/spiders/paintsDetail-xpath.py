# -*- coding: utf-8 -*-
import scrapy


class ToScrapeSpiderXPath(scrapy.Spider):
    name = 'paintsDetail-xpath'
    start_urls = []
    file_object = open('E:/code/KGQA_painter-master/quotesbot/quotesbot/data/txt/paints.txt', 'r', encoding="utf-8").readlines()

    for data in file_object:  #生成url列表
        start_urls.append(data.strip('\n').split(" ")[-1])
    print(start_urls)
    def parse(self, response):
        for quote in response.xpath('//div[@class="det1 clearfix"]//div[@class="wrap"]//div[@class="text"]'):
            yield {
                'name': quote.xpath('./h3/text()').extract_first(),
                'detail': quote.xpath('.//div[@class="p"]/p/text()').extract()

            }
        for quote in response.xpath('//div[@class="det1 clearfix det4"]//div[@class="wrap"]//div[@class="cont"]'):
            yield {
                'name': quote.xpath('.//div[@class="text"]/h3/text()').extract_first(),
                'detail': quote.xpath('.//div[@class="text"]//div[@class="p"]/p/text()').extract()

            }



