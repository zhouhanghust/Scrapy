# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.pipelines.images import ImagesPipeline
from scrapy.exceptions import DropItem
from scrapy.http import Request
import re

class XianPipeline(object):

    # def get_meta_requests(self, item, info):
    #     for image_url in item['ImgUrl']:
    #         yield Request(image_url, meta={'item':item['name']})
    #
    # def file_path(self, request, response=None, info=None):
    #     name = request.meta['item']
    #     name = re.sub(r' [?\\*|<>:/()123456789]','',name)
    #     image_guid = request.url.split("/")[-1]
    #     filename = u'full/{0}_{1}'.format(name, image_guid)
    #     return filename
    #
    # def item_completed(self, results, item, info):
    #     image_path = [x['path'] for ok, x in results if ok]
    #     if not image_path:
    #         raise DropItem("Item contains no images")
    #     item['image_paths'] = image_path
    #     return item
    
    def process_item(self, item, spider):
        return item