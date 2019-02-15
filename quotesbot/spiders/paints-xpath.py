# -*- coding: utf-8 -*-
import scrapy


class ToScrapeSpiderXPath(scrapy.Spider):
    name = 'paints-xpath'
    start_urls = [
        'https://www.dpm.org.cn/collection/paints.html',
    ]

    def parse(self, response):
        i=0
        print("enter parse=========================")
        for quote in response.xpath('//div[@class="table1"]//table/tbody/tr'):
            i=i+1
            print("==========",i)
            yield {
                'href': quote.xpath('.//td[1]/a/@href').extract_first(),
                'image': quote.xpath('.//td[1]/a//div[@class="img"]/img/@src').extract_first(),
                'name': quote.xpath('.//td[1]/a/text()').extract_first(),
                'epoch': quote.xpath('.//td[2]/text()').extract_first(),
                'classification': quote.xpath('.//td[3]/text()').extract_first(),
                'author': quote.xpath('.//td[4]/text()').extract_first()
            }

        next_page_url = response.xpath('//a[@class="next"]/@href').extract_first()
        if next_page_url is not None:
            print("next_page_url",next_page_url)
            yield scrapy.Request(response.urljoin(next_page_url))

