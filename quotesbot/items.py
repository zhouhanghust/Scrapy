# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class QuotesbotItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
class DmozItem(scrapy.Item):
    title = scrapy.Field()
    link = scrapy.Field()
    desc = scrapy.Field()


class BaiduItem(scrapy.Item):
    # Item 对应互动百科中的一个词条
    title = scrapy.Field()  #标题
    url = scrapy.Field()  #对于百度百科页面的链接
    image = scrapy.Field()  #博物馆图片
    detail = scrapy.Field()  #详细信息
    baseInfoKeyList = scrapy.Field()  #基本信息key列表
    baseInfoValueList = scrapy.Field()  #基本信息value列表


class MuseumItem(scrapy.Item):
    museumName  = scrapy.Field()
    englishName  = scrapy.Field()
    summary = scrapy.Field()
    image = scrapy.Field()
    baikeUrl = scrapy.Field()
    location  = scrapy.Field()
    category  = scrapy.Field()
    address  = scrapy.Field()
    completionDate  = scrapy.Field()
    openingHours  = scrapy.Field()
    collectionBoutique  = scrapy.Field()
    incumbentCurator  = scrapy.Field()
    generalDesigner  = scrapy.Field()
    ownedDepartment  = scrapy.Field()
    ownedCountry  = scrapy.Field()
    ownedCity  = scrapy.Field()
    ticketPrice = scrapy.Field()
    suggestedPlayingTime = scrapy.Field()
    suitableSeason = scrapy.Field()
    totalArea = scrapy.Field()
    level = scrapy.Field()
    firstOpeningDate = scrapy.Field()

class PainterItem(scrapy.Item):
    title = scrapy.Field()  #标题
    url = scrapy.Field()  #对于百度百科页面的链接
    image = scrapy.Field()  #人物图片
    detail = scrapy.Field()  #详细信息，简介
    baseInfoKeyList = scrapy.Field()  #基本信息key列表
    baseInfoValueList = scrapy.Field()  #基本信息value列表
    chronology = scrapy.Field() #年表
    major_works = scrapy.Field() #主要作品
    character = scrapy.Field() #作品特点
    relation = scrapy.Field() #人物关系
    social_evaluation = scrapy.Field() #社会评价