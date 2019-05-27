# -- coding: utf-8 --
import scrapy
import re
import time
from scra.items import ScraItem
class scrapy_xm(scrapy.Spider):


    name = 'scrapy_xm'
    start_urls = ['https://www.acfun.cn/']
    def parse(self,response):
        # body = response.body
        # unicode_body = response.body_as_unicode()
        item = ScraItem()
        selector = scrapy.Selector(response)

        day_titles = selector.xpath('//*[@id="main"]/section[3]/div[1]/div[1]/div[1]/figure[*]/figcaption/b/a/@title')
        item['title'] = response.xpath('//*[@id="main"]/section[3]/div[1]/div[1]/div[1]/figure[*]/figcaption/b/a/@title').extract()
        # print(type(item['title']))
        for each in day_titles:
            title = each.extract()
            print(each)
        yield item
            # save = str(title+"\r\n")
            # with open('scrapy.txt', 'ab') as f:
            #     f.write(save.encode('utf-8'))



