# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ScraAbcItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    up = scrapy.Field()
    play = scrapy.Field()
    title = scrapy.Field()
    danmu = scrapy.Field()
    comments = scrapy.Field()
    pass
