# -*- coding: utf-8 -*-
import scrapy


class PiratebaySpider(scrapy.Spider):
    name = "piratebay"
    #allowed_domains = ["thepiratebay.org/browse/200"]
    #start_urls = ['https://thepiratebay.org/browse/200/']
    start_urls = [
            # movie links top 5 hot list
            'https://thepiratebay.org/browse/201/0/7',
            'https://thepiratebay.org/browse/201/1/7',
            'https://thepiratebay.org/browse/201/2/7',
            'https://thepiratebay.org/browse/201/3/7',
            'https://thepiratebay.org/browse/201/4/7',
            # Moive clip links top 2 hot list
            'https://thepiratebay.org/browse/501/0/7',
            'https://thepiratebay.org/browse/501/1/7',
            ]
    #https://thepiratebay.org/browse/201/0/7

    g_subPages = 0
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
        '''
        if g_subPages!=0:
            pass
        g_subPages=1

        i = 0
	for item in response.xpath('//tr//td[@colspan]//a[not(img)]'):
		next_page = item.xpath("@href").extract_first();
		next_page = response.urljoin(next_page) + "/"
		print next_page
                if i>=5:
                    break
		yield scrapy.Request(next_page, callback=self.parse)
                i+=1
        '''
        #pass
