# -*- coding: utf-8 -*-
import scrapy


class PiratebaySpider(scrapy.Spider):
    name = "piratebay"
    #allowed_domains = ["thepiratebay.org/browse/200"]
    start_urls = ['https://thepiratebay.org/browse/200/']

    def parse(self, response):
        for item in response.xpath('//tr//td[*//@alt="Magnet link"]'):
                #print item
                title = item.xpath("div/a/text()").extract_first()
                mganetlink = item.xpath("a/@href").extract_first()
		mganetlink = response.urljoin(mganetlink)
                bt_info = {"title":title, "link":mganetlink}
                print bt_info
                yield {
                        "title": title,
                        "link": mganetlink
                }
	for item in response.xpath('//tr//td[@colspan]//a[not(img)]'):
		next_page = item.xpath("@href").extract_first();
		next_page = response.urljoin(next_page) + "/"
		print next_page
		yield scrapy.Request(next_page, callback=self.parse)
        #pass
