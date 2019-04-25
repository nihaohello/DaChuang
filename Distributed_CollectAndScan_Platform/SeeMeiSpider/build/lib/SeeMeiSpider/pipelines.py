# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from index.models import Feeds

class SeemeispiderPipeline(object):
    def process_item(self, item, spider):
    	if "?" in item["url"] and "=" in item["url"]:
        	item.save()
        	return item

