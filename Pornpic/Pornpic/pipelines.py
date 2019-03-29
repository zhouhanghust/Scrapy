# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.pipelines.images import ImagesPipeline
from scrapy.exceptions import DropItem
from scrapy import Request
import re


class PornpicPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        for img_url in item['ImgUrl']:
            yield Request(img_url, meta={"item": item['name']})

    def file_path(self, request, response=None, info=None):

        name = request.meta['item']
        name = re.sub(r'[？\\*|“<>:/()0123456789]', '', name)
        image_guid = request.url.split('/')[-1]
        # name2 = request.url.split('/')[-2]
        filename = u'full/{0}/{1}'.format(name, image_guid)
        filename = u'full/%s_%s' % (name, image_guid)
        return filename

    def item_completed(self, results, item, info):
        img_path = [x['path'] for ok, x in results if ok]
        if not img_path:
            raise DropItem('Item contains no images')
        item['image_paths'] = img_path
        return item
