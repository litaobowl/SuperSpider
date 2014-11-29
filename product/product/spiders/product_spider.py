import scrapy

from datetime import datetime
from product.items import ProductItem
from product.items import ProductDetailItem
from product.items import ProductDescItem

class ProductSpider(scrapy.Spider): 
    name = "product"
    allowed_domains = ["www.6pm.com"]
    start_urls = [
	"http://www.6pm.com/handbags~4P#!/handbags~4?p=1&s=goliveRecentSalesStyle/desc/"]
    
    def parse(self, response):
	for sel in response.xpath('//div[contains(@id,"searchResults")]//a'):
		productItem = ProductItem()
		item = ProductDetailItem()
		item['retailer'] = '6pm US'
		item['brand'] = str(sel.xpath('span[contains(@class,"brandName")]/text()').extract()[0])
		link = sel.xpath('@href').extract()[0]
		item['price'] = str(sel.xpath('span[contains(@class,"price-6pm")]/text()').extract()[0])
		item['product_name'] = str(sel.xpath('span[contains(@class,"productName")]/text()').extract()[0]) 
		item['product_url'] = str(link)
		item['product_image_url'] = str(sel.xpath('img/@src').extract()[0])
		i = datetime.now()
		item['created'] = i.strftime('%Y/%m/%d %H:%M:%S') 
		item['last_modified'] = i.strftime('%Y/%m/%d %H:%M:%S')
		productItem['product'] = item
		request = scrapy.Request('http://www.6pm.com'+ link,
                             callback=self.parse_page2)
		request.meta['item'] = productItem
    		yield request

    def parse_page2(self, response):
	description = ''
	additional_field = ''
	productItem = response.meta['item']
	descItem = ProductDescItem()
    	for sel in response.xpath('//div[contains(@class,"description")]//ul//li[not(@class)]'):
		description = description + sel.xpath('text()').extract()[0]
	descItem['description'] = description
	for sel in response.xpath('//div[contains(@class,"description")]/ul//li[contains(@class, "measurement")]'):
		additional_field = additional_field + sel.xpath('text()').extract()[0]
	descItem['additional_field'] = str(additional_field)	
	productItem['product_desc'] = descItem
    	return productItem
