# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.pipelines.images import ImagesPipeline
from scrapy.exceptions import DropItem
from scrapy import Request
import re
import urllib.request
import os

class XianPipeline(object):

    def get_meta_requests(self, item, info):
        for image_url in item['ImgUrl']:
            yield Request(image_url, meta={'item':item['name']})

    def file_path(self, request, response=None, info=None):
        name = request.meta['item']
        name = re.sub(r' [?\\*|<>:/()123456789]','',name)
        image_guid = request.url.split("/")[-1]
        filename = u'full/{0}_{1}'.format(name, image_guid)
        return filename

    def item_completed(self, results, item, info):
        image_path = [x['path'] for ok, x in results if ok]
        if not image_path:
            raise DropItem("Item contains no images")
        # item['image_paths'] = image_path
        return item

    # def process_item(self, item, spider):
    #     imgpath = os.path.dirname(__file__)
    #     IMAGES_STORE = os.path.join(imgpath, 'images')
    #     for image_url in item['ImgUrl']:
    #         if image_url is not None:
    #             name = item['name']
    #             image_guid = image_url.split("/")[-1]
    #             filename = u'full/{0}_{1}'.format(name, image_guid)
    #             filename = os.path.join(IMAGES_STORE, filename)
    #
    #             urllib.request.urlretrieve(image_url, filename=filename)
    #     return item