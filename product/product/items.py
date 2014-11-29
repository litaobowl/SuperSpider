# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ProductItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #title = scrapy.Field()
    brand = scrapy.Field()
    retailer= scrapy.Field()
    #description = scrapy.Field()
    #price = scrapy.Field()
    #sale_price = scrapy.Field()
    #status = scrapy.Field()
    #product_url = scrapy.Field()
    #product_image_url = scrapy.Field()
    

