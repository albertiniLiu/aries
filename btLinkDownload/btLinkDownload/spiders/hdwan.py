# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class HdwanSpider(CrawlSpider):
    name = 'hdwan'
    allowed_domains = ['hdwan.net']
    start_urls = ['http://www.hdwan.net/']
    #start_urls = ['http://http://hdwan.net/']

    rules = (
        Rule(LinkExtractor(allow=r'Items/'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        i = []
        print "inside parse_item======================================"
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        btlinks = sel.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "entry-title", " " ))]//  a')
        for btlink in btlinks:
            url = btlink.xpath("@href").extract_first()
            name = btlink.xpath("text()").extract_first().split("]")[0][1:]
            mItem["url"]= url
            mItem["name"]= name
            i.append(mItem)
        for item in i:
            print item
        return i
