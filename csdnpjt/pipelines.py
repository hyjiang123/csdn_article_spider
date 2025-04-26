# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
import logging
# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from numpy import histogram


class CsdnpjtPipeline:
    def __init__(self):
        # 下面的参数需要替换为实际数据库的相关参数
        self.conn = pymysql.connect(host="ip",user="username",password="password",db="db_name",port=port)

    def process_item(self, item, spider):
        for j in range(0, len(item["name"])):
            name = item["name"][j]
            url = item["url"][j]
            hits = item["hits"][j]
            hits = str(hits)
            comment = item["comment"][j]
            comment = str(comment)
            sql = "insert into csdndemo(name, url, hits, comment) VALUES('"+name+"','"+url+"','"+hits+"','"+comment+"')"

            cs = self.conn.cursor()
            cs.execute(sql)
            self.conn.commit()
        return item

    def close_spider(self, spider):
        self.conn.close()
