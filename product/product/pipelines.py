# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo
from scrapy.conf import settings
from scrapy import log
class ProductPipeline(object):
    def process_item(self, item, spider):
        return item

class MongoDBPipeline(object):
    def __init__(self):
        connection = pymongo.Connection(settings['MONGODB_SERVER'], settings['MONGODB_PORT'])
        db = connection[settings['MONGODB_DB']]
	self.collection = {}
        self.collection['product'] = db[settings['MONGODB_COLLECTION']]
	self.collection['desc'] = db[settings['MONGODB_COLLECTION1']]
        
    def process_item(self, item, spider):
	valid = True
        for data in item:
       	  if not data:
            valid = False
            raise DropItem("Missing %s of blogpost from %s" %(data, item['url']))
        if valid:
          self.collection['product'].insert(dict(item['product']))
	  self.collection['desc'].insert(dict(item['product_desc']))
          log.msg("Item wrote to MongoDB database %s/%s" %
                  (settings['MONGODB_DB'], settings['MONGODB_COLLECTION']),
                  level=log.DEBUG, spider=spider) 
        return item
