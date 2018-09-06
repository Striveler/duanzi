# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from duanzi.items import DuanziItem


class XiaohuaSpider(CrawlSpider):
    name = 'xiaohua'
    allowed_domains = ['neihan8.com']
    start_urls = ['https://www.neihan8.com/wenzi/index.html']

    rules = (
        Rule(LinkExtractor(allow=r'index\_?\d?')),
        Rule(LinkExtractor(allow=r'com\/\w+\/\d+.html') ,callback='parse_item', follow=True))
    

    def parse_item(self, response):
        item = DuanziItem()
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        item['name'] = response.xpath('//h1/text()').extract()[0]
        item['content'] = response.xpath('//div[@class="detail"]/p/text()').extract()[0]
        #item['link'] = response.xpath('').extract[0]
        item['link'] = response.url
        yield item
