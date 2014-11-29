import scrapy

from product.items import ProductItem

class ProductSpider(scrapy.Spider): 
    name = "product"
    allowed_domains = ["6pm.com"]
    start_urls = [
	"http://www.6pm.com/handbags~4P#!/handbags~4?p=1&s=goliveRecentSalesStyle/desc/"]
    
    def parse(self, response):
	for sel in response.xpath('//div[contains(@id,"searchResults")]'):
		item = ProductItem()
		item['brand'] = sel.xpath('a/span[contains(@class,"brandName")]/text()').extract()
		yield item
