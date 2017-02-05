# -*- coding: utf-8 -*-
import scrapy


class HdwanbasicSpider(scrapy.Spider):
    name = "hdwanbasic"
    allowed_domains = ["www.hdwan.net"]
    #start_urls = ['http://www.hdwan.net/39889.html']
    start_urls = ['http://www.hdwan.net/']

    def parse(self, response):
        print "================================"
        pages=[]
        import pdb
        pdb.set_trace()
        btlinks = response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "article", " " ))]//a')
        for btlink in btlinks:
            mItem={}
            url = btlink.xpath("@href").extract_first()
            name = btlink.xpath("text()").extract_first().split("]")[0][1:]
            mItem["url"]= url
            mItem["name"]= name
            pages.append(mItem)
        print len(pages)
        for item in pages:
            print item
        pass
