# -*- coding: utf-8 -*-
import scrapy
from quotesbot.items import BaiduItem
import urllib

split_sign = '##'  # 定义分隔符
class ToScrapeSpiderXPath(scrapy.Spider):
    name = 'allperson-xpath'
    start_urls = []
    file_object = open('data/txt/painter.txt', 'r', encoding="utf-8").read()
    wordList = file_object.split("\n")  # 获取词表
    for i in wordList:  ##生成url列表
        cur = "https://baike.baidu.com/item/"
        cur = cur + str(i)
        start_urls.append(cur)

    def parse(self, response):
        print("enter parse")
        # div限定范围
        main_div = response.xpath('//div[@class="content-wrapper"]')

        url = response.url  # url直接得到
        url = urllib.parse.unquote(url)

        title = "error"
        if url.find('error') != -1:
            print("百科中找不到对应页面！")
            title = "error"
        else:
            title = response.url.split('item/')[-1]  # 通过截取url获取title
            title = urllib.parse.unquote(title)

            if title.find('fromtitle') != -1:
                print("=====fromtitle========", title)
                title = title.split('fromtitle=')[-1].split('&')[0]
            if title.find("/")!=-1:
                title = title.split('/')[0]

        img = ""  # 爬取图片url
        for p in main_div.xpath(
                './/div[@class="content"]/div[@class="side-content"]/div[@class="summary-pic"]/a/img/@src'):
            img = p.extract().strip()


        detail = ""  # 详细信息
        for detail_xpath in main_div.xpath('.//div[@class="lemma-summary"]/div[@class="para"]'):
            detail += detail_xpath.xpath('string(.)').extract()[0].strip()


        flag = 0
        baseInfoKeyList = ""  # 基本信息的key值
        for dl in main_div.xpath('.//div[@class="basic-info cmn-clearfix"]/dl'):
            for p in dl.xpath('dt'):
                if flag == 1:
                    baseInfoKeyList += split_sign
                print(p.xpath('string(.)').extract()[0])
                baseInfoKeyList += p.xpath('string(.)').extract()[0].replace("&nbsp;","").strip()
                flag = 1
        print("baseInfoKeyList", baseInfoKeyList)
        ## 继续调xpath！！！！！！！！！！！！！
        flag = 0
        baseInfoValueList = ""  # 基本信息的value值
        for dl in main_div.xpath('.//div[@class="basic-info cmn-clearfix"]/dl'):
            for p in dl.xpath('dd'):
                print("baseInfoValueList enter ")
                if flag == 1:
                    baseInfoValueList += split_sign
                all_text = p.xpath('string(.)').extract()[0].strip()
                baseInfoValueList += all_text
                flag = 1
        print("baseInfoValueList", baseInfoValueList)
        item = BaiduItem()
        item['title'] = title
        item['url'] = url
        item['image'] = img
        item['detail'] = detail
        item['baseInfoKeyList'] = baseInfoKeyList
        item['baseInfoValueList'] = baseInfoValueList

        yield item

