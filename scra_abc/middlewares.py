# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
from scrapy.http import HtmlResponse
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from logging import getLogger
import time
global n

class ScraAbcSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class ScraAbcDownloaderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)

class SeleMiddleware(object):

    def __init__(self, timeout=30, isLoadImage=True, windowHeight=None, windowWidth=None):
        self.logger = getLogger(__name__)
        self.timeout = timeout
        self.isLoadImage = isLoadImage
        # 定义一个属于这个类的browser，防止每次请求页面时，都会打开一个新的chrome浏览器
        # 这样，这个类处理的Request都可以只用这一个browser
        chrome_options = Options()
        self.browser = webdriver.Chrome(chrome_options=chrome_options,
                                  executable_path='C:\Program Files (x86)\Google\Chrome\Application\chromedriver')
        if windowHeight and windowWidth:
            self.browser.set_window_size(900, 900)
        self.browser.set_page_load_timeout(self.timeout)  # 页面加载超时时间
        self.wait = WebDriverWait(self.browser, 25)  # 指定元素加载超时时间

    def process_request(self, request, spider):
        self.browser.get(request.url)
        handle = self.browser.current_window_handle
        time.sleep(3)
        global n
        if request.url == 'https://www.acfun.cn/':
            n=1
            WebDriverWait(self.browser, 3).until(EC.presence_of_all_elements_located((By.ID, 'search-text')))
            self.browser.find_element_by_xpath('//*[@id="search-text"]').clear()
            self.browser.find_element_by_xpath('//*[@id="search-text"]').send_keys("全战三国")
            self.browser.find_element_by_xpath('//*[@id="search-btn"]/i').click()
            handles = self.browser.window_handles
            # 对窗口进行遍历
            for newhandle in handles:
                # 筛选新打开的窗口B
                if newhandle != handle:
                    self.browser.switch_to.window(newhandle)
            WebDriverWait(self.browser, 5).until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'list-wrap')))
        else:
            if(n<5):
                self.browser.find_element_by_xpath('//*[@id="list-pager"]/div/span[8]').click()
                n+=1
            else:
                self.browser.find_element_by_xpath('//*[@id="list-pager"]/div/span[10]').click()
                n+=1
            time.sleep(2)
        # handles = self.browser.window_handles
        # # 对窗口进行遍历
        # for newhandle in handles:
        #     # 筛选新打开的窗口B
        #     if newhandle != handle:
        #         self.browser.switch_to.window(newhandle)
        # WebDriverWait(self.browser, 5).until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'list-wrap')))
        print(self.browser.current_url)
        return HtmlResponse(url=self.browser.current_url, body=self.browser.page_source, encoding="utf-8")
            # self.browser.find_element_by_xpath('//*[@id="list-pager"]/div/span[8]/i').click()





