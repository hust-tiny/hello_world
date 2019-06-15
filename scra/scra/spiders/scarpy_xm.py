# -- coding: utf-8 --
import scrapy
from scrapy.http import Request
from scra.items import ScraItem



class scrapy_xm(scrapy.Spider):
    name = 'scrapy_xm'
    start_urls = ['https://www.acfun.cn/member/#area=splash']

    def start_requests(self):
        yield Request('https://www.acfun.cn/member/#area=splash',meta={'cookiejar': 'chrome'})
        #print('123')


    def parse(self,response):
        item = ScraItem()
        selector = scrapy.Selector(response)

        day_titles = selector.xpath('//*[@id="header-guide"]/li[1]/span/text()').extract()
        #item['title'] = response.xpath('//*[@id="main"]/section[3]/div[1]/div[1]/div[1]/figure[*]/figcaption/b/a/@title').extract()
        # for each in day_titles:
        #     title = each.extract()
        #     print(each)
        print(day_titles)
        #yield item
            # save = str(title+"\r\n")
            # with open('scrapy.txt', 'ab') as f:
            #     f.write(save.encode('utf-8'))



