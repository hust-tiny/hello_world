# -*- coding: utf-8 -*-
import csv
import pymongo
import re
import pymysql.cursors
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class ScraAbcPipeline(object):
    def process_item(self, item, spider):

        return item


class CsvPipeline(object):
    def process_item(self, item, spider):
        with open('scrapy.csv','a',encoding='utf-8',newline='') as csvfile:
            spamwriter = csv.writer(csvfile,dialect=("excel"),encoding='utf-8')
            playlist = []
            danmulist = []
            plays = item['play']
            for play in plays:
                playre = re.sub(r"\D","",play)
                playlist.append(playre)
            danmus = item['danmu']
            for danmu in danmus:
                danmure = re.sub(r"\D","",danmu)
                danmulist.append(danmure)
            rows = zip(item['title'], item['up'], playlist,
                             danmulist)
            for row in rows:
                spamwriter.writerow(row)
        return item



class MongoPipeline(object):
    collection = 'quanzhansanguo'
    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls,crawler):
        return cls(
            mongo_uri = crawler.settings.get('MONGO_URI'),#获取MONGO数据库的本地URI，在setting里面已声明
            mongo_db = crawler.settings.get('MONGO_DB')#获取数据库名，也在setting里面声明好了
        )
    #打开连接
    def open_spider(self,spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]
    #关闭连接
    def close_spider(self,spider):
        self.client.close()
    #mongo的数据写入是独特的，跟Mysql之类的数据库写入语言不同，需要时可以查阅相关文档，在readme.txt里面会给出链接，有兴趣也可以查一下Mysql跟Mongo的异同。
    def process_item(self,item,spider):
        titles = item['title']
        table = self.db[self.collection]
        postitem = dict(item)
        table.insert(postitem)
        return item
