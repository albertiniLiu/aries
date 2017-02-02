# -*- coding: utf-8 -*-
import scrapy


class HdwanbasicSpider(scrapy.Spider):
    name = "hdwanbasic"
    allowed_domains = ["www.hdwan.net"]
    start_urls = ['http://www.hdwan.net/']

    def parse(self, response):
        print "================================"
        i=[]
        btlinks = response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "article", " " ))]//a')
        import pdb
        pdb.set_trace()
        for btlink in btlinks:
            url = btlink.xpath("@href").extract_first()
            name = btlink.xpath("text()").extract_first().split("]")[0][1:]
            mItem["url"]= url
            mItem["name"]= name
            i.append(mItem)
        for item in i:
            print item
        pass
