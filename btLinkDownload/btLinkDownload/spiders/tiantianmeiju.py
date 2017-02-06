# -*- coding: utf-8 -*-
import scrapy


class TiantianmeijuSpider(scrapy.Spider):
    name = "tiantianmeiju"
    allowed_domains = ["www.ttmeiju.com/summary.html"]
    start_urls = ['http://www.ttmeiju.com/summary.html/']

    def parse(self, response):
        sp = []
        urls = []
        for i in range(6, 156):
            cp = "/html/body/div[@id='wrapper']/div[@id='midder']/div[@class='content']/div[@class='contentbox']/table[@class='seedtable']/tr[%d]/td[2]/a/" % i
            sp.append(cp)

        for cp in sp:
            title= response.xpath(cp + "/text()").extract()
            url= response.xpath(cp + "/@href").extract()
            urls.append({'title':title, 'url':url})

        for url in urls:
            print url
        pass
