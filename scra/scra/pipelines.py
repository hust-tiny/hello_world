# -*- coding: utf-8 -*-

# Define your item pipelines here
import pymongo
import pymysql.cursors

import re
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class ScraPipeline(object):
    def process_item(self, item, spider):
        #txt文档写入
        # with open('scrapy.txt','w',encoding='utf-8') as f:
        titles = item['title']
        #     # numbers = item['number']
        for i in titles:
            title_str = str(i+'\r\n')
            title_list = title_str.split("UP:",-1)
            title_list2 = title_list[1].split("发布于")
            title_list3 = title_list2[1].split("/")
        #         f.write(title_list[0]+'\r\n'+title_list2[0]+'\r\n'+title_list3[0]+title_list3[1]+title_list3[2])
            self.cursor.execute(
                 """insert into acfun(title,up,day_time,click,comment)
                value(%s,%s,%s,%s,%s)""",
                    (title_list[0],title_list2[0],title_list3[0],title_list3[1],title_list3[2],)
                            )
            self.connect.commit()
        return item

#Mysql数据库连接设置
    def __init__(self):
        # 连接数据库
        self.connect = pymysql.connect(
            host='localhost',  # 数据库地址
            port=3306,  # 数据库端口
            db='scrapy',  # 数据库名
            user='root',  # 数据库用户名
            passwd='781950712',  # 数据库密码
            charset='utf8',  # 编码方式
            use_unicode=True)

        # 通过cursor执行增删查改
        self.cursor = self.connect.cursor();

# csv写入
class CsvPipeline(object):
    pass

# excle写入
class ExclePipeline(object):
    pass

#Mysql数据库连接设置
class MysqlPipeline(object):

    def __init__(self):
        # 连接数据库
        self.connect = pymysql.connect(
            host='localhost',  # 数据库地址
            port=3306,  # 数据库端口
            db='scrapy',  # 数据库名
            user='root',  # 数据库用户名
            passwd='781950712',  # 数据库密码
            charset='utf8',  # 编码方式
            use_unicode=True)

        # 通过cursor执行增删查改
        self.cursor = self.connect.cursor();

    def process_item(self, item, spider):
        titles = item['title']
        #     # numbers = item['number']
        for i in titles:
            title_str = str(i+'\r\n')
            title_list = title_str.split("UP:",-1)
            title_list2 = title_list[1].split("发布于")
            title_list3 = title_list2[1].split("/")
            self.cursor.execute(
                 """insert into acfun(title,up,day_time,click,comment)
                value(%s,%s,%s,%s,%s)""",
                    (title_list[0],title_list2[0],title_list3[0],title_list3[1],title_list3[2],)
                            )
            self.connect.commit()
        return item
    pass


class MongoPipeline(object):
    collection = 'dayli'

    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls,crawler):
        return cls(
            mongo_uri = crawler.settings.get('MONGO_URI'),
            mongo_db = crawler.settings.get('MONGO_DB')
        )

    def open_spider(self,spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def close_spider(self,spider):
        self.client.close()

    def process_item(self,item,spider):
        titles = item['title']
        table = self.db[self.collection]
        for i in titles:
            data = {}
            data_list = str(i).split("UP:")
            print(data_list[0])
            data_list2 = data_list[1].split("发布于")
            data_list3 = data_list2[1].split("/")
            data['文章：'] = data_list[0]
            data['UP：'] = data_list2[0]
            data['时间：'] = data_list3[0]
            data['点击：'] = data_list3[1]
            data['评论'] = data_list3[2]
            table.insert_one(data)
        return item