# -- coding: utf-8 --
import scrapy
from scrapy import Request

import re
from scrapy.linkextractors import LinkExtractor
from scra_abc.items import ScraAbcItem
from scrapy.http import HtmlResponse
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
global n

class quanzhansanguo(scrapy.Spider):
    name = 'quanzhansanguo'
    # start_urls = ["https://www.acfun.cn/"]

    def start_requests(self):
        global n
        n=0
        start_urls = ["https://www.acfun.cn/"]
        for url in start_urls:
            yield Request(url=url, callback=self.parse,dont_filter=True)


    def parse(self, HtmlResponse):
        item = ScraAbcItem()
        selector = scrapy.Selector(HtmlResponse)
        list = []
        global n
        n+=1
        # item['title'] = selector.xpath('//div[@class="video-cell-right fl cell-right"]/div[@class="title"]/a[descendant-or-self::text()]').extract()
        # print(item['title'])
        datas = selector.xpath('//div[@class="video-cell-right fl cell-right"]/div[@class="title"]/a')
        for data in datas:
            list.append(data.xpath('string(.)').extract()[0])
        item['title'] = list
        item['up'] = selector.xpath('//div[@class="video-cell-right fl cell-right"]/ul/li[2]/a/text()').extract()
        item['play'] = selector.xpath('//div[@class="video-cell-right fl cell-right"]/ul/li[3]/text()').extract()
        item['danmu'] = selector.xpath('//div[@class="video-cell-right fl cell-right"]/ul/li[4]/text()').extract()
        yield item
        print(item['title'])
        if n<20:
            yield Request(url=HtmlResponse.url,callback=self.parse,dont_filter=True)
        # print(len(item['title']))
