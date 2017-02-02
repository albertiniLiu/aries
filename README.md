# aries
This is my web crawler project

steps to create scrapy project
1. download scrapy code frome github
  git clone git@github.com:albertiniLiu/aries.git
  cd aries/btLinkDownload/

2. install vps client
  sudo add-apt-repository ppa:hzwhuang/ss-qt5
  sudo apt-get update
  sudo apt-get install shadowsocks-qt5
  sudo apt-get install proxychains

3. using vps client to web browser
  ss-qt5 &
  proxychains chromium-browser &

4. install scrapy  https://doc.scrapy.org/en/latest/intro/tutorial.html
  pip install Scrapy

5. using scrapy
    scrapy startproject btLinkDownload
.
├── btLinkDownload
│   ├── __init__.py
│   ├── __init__.pyc
│   ├── items.py
│   ├── middlewares.py
│   ├── pipelines.py
│   ├── settings.py
│   ├── settings.pyc
│   └── spiders
│       ├── __init__.py
│       ├── __init__.pyc
│       ├── piratebay.py
│       └── piratebay.pyc
├── result.json
└── scrapy.cfg

6. write scrapy code
now let's do one example for http://www.hdwan.net
Generate spider file using scrapy tool:
scrapy genspider -t crawl hdwan http://hdwan.net
it will generate ./btLinkDownload/spiders/hdwan.py

7. write spider code and verify
first using scrpy shell to debug xpath url
scrapy shell www.hdwan.net
and then I can check using several commands:
view(response)
this command can show webpage on web browser which scrapy get from scrapy shell command

and then we can use web browser to get xpath code using selectorGagdet
selectorGadget can get xpath in several click, please learn it by yourself
such as I get movie url by
btlinks = sel.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "entry-title", " " ))]//a')
and then verify this xpath in scrapy shell
btlinks present one movie item
>>> btlinks[0].extract()
u'<a href="http://www.hdwan.net/39263.html" rel="bookmark" itemprop="name">[\u94a2\u94c1\u9a91\u58eb/\u8d85\u80fd\u91cf\u6218\u58eb][2016][\u6b27\u7f8e][\u79d1\u5e7b][BD-MKV/2G][\u82f1\u8bed/\u7b80\u7e41\u4e2d\u82f1\u5b57\u5e55][720P.BluRay\u66f4\u65b0]</a>'

now extract url and movie title using below xpath method
>>> btlinks[0].xpath("@href").extract_first()
u'http://www.hdwan.net/39263.html'
>>> btlinks[0].xpath("text()").extract_first().split("]")[0][1:]
u'\u94a2\u94c1\u9a91\u58eb/\u8d85\u80fd\u91cf\u6218\u58eb'

now we get next url link
>>> nextPage = sel.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "next", " " ))]')
>>> nextPage.xpath("@href")
[<Selector xpath='@href' data=u'http://www.hdwan.net/page/2'>]
>>> nextPage.xpath("@href").extract_first()


