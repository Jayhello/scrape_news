# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
# import pymongo
from scrapy.conf import settings
from scrapy.exceptions import DropItem
import MySQLdb
from utils.stringreg import str_related
import json
from utils.log import get_logger


class MysqlPipeline(object):

    path = '../config/logging.json'
    log = get_logger(path)

    def __init__(self):
        # self.init_log()
        self.config_db()

    def process_item(self, item, spider):
        try:
            url = item['url'].encode('utf-8')
            title = item['title'].encode('utf-8')
            scrape_date = item['scrape_date'].encode('utf-8')
            web_src = item['web_src'].encode('utf-8')
            webname = item['webname'].encode('utf-8')
            webtype = item['webtype'].encode('utf-8')
            web_src_url = item['web_src_url'].encode('utf-8')

            tb_common = self.tb_common.encode('utf-8')
            tb_yynews = self.tb_yynews.encode('utf-8')

            SELCT_IF_EXIST = "SELECT * FROM %s WHERE url = '%s';"
            rows_tb1 = self.cursor.execute(SELCT_IF_EXIST % (tb_common, url))

            if rows_tb1 == 0:
                SELCT_IF_EXIST_TITLE = "SELECT * FROM %s WHERE title = '%s';"
                rows_tb11 = self.cursor.execute(SELCT_IF_EXIST_TITLE % (tb_common, title))
                if rows_tb11 == 0:
                    sql = "insert into "+tb_common+" (url, title, scrape_date, web_src) values(%s, %s, %s, %s)"
                    # sql = "insert into "+tb_common+" (url, news_title, news_date, web_src) values(%s, %s, %s, %s)"
                    self.cursor.execute(sql, (url, title, scrape_date, web_src))

            b_releated = str_related(title, webtype)
            rows_tb2 = 0
            if b_releated:
                rows_tb2 = self.cursor.execute(SELCT_IF_EXIST % (tb_yynews, url))
                if rows_tb2 == 0:
                    SELCT_IF_EXIST_TITLE = "SELECT * FROM %s WHERE news_title = '%s';"
                    rows_tb22 = self.cursor.execute(SELCT_IF_EXIST_TITLE % (tb_yynews, title))
                    # sql_yylive = "insert into "+tb_yynews+" (url, title, scrape_date, web_src) values(%s, %s, %s, %s)"
                    if rows_tb22 == 0:
                        insert_fields_lst = " (url, news_title, news_date, create_date, web_src, news_type, web_src_name,web_src_url) values(%s, %s, %s,%s, %s, %s,%s, %s)"
                        sql_yylive = "insert into " + tb_yynews + insert_fields_lst
                        self.cursor.execute(sql_yylive, (url, title, scrape_date, scrape_date, web_src, webtype, webname, web_src_url))

            if rows_tb1 == 0 or (b_releated is True and 0 == rows_tb2):
                self.conn.commit()

        except MySQLdb.Error, e:
            MysqlPipeline.log.error("error %d: %s" % (e.args[0], e.args[1]))

    def config_db(self):
        jsonfile = 'run_config/mysql_config.json'
        # jsonfile = 'run_config/test_mysql_config.json'
        with open(jsonfile) as json_file_data:
            data = json.load(json_file_data)

        host = data['host']
        user = data['user']
        pwd = data['pwd']
        db = data['db']
        port = data['port']
        self.tb_common = data['tb_common']
        self.tb_yynews = data['tb_yynews']

        self.conn = MySQLdb.connect(host=host, port=port, user=user, passwd=pwd, db=db, charset="utf8", use_unicode=True)
        self.cursor = self.conn.cursor()

    # def init_log(self):
    #     path = '../config/logging.json'
    #     self.logger = get_logger(path)

    def query(self):
        """
        the function is just for test
        :return:
        """
        try:
            sql = 'select * from scrape_yy'
            self.cursor.execute(sql)
            print self.cursor.fetchall()

            url = '1http://www.junjiewang.com/hulianwang/45660.html'
            title = '111111111111111111'
            scrape_date = '2017-02-27 18:27:17'
            web_src = 'junjie'
            tb_common = 'scrape_yy'
            tb_yynews = 'yylive_news'
            SELCT_IF_EXIST = "SELECT * FROM %s WHERE url = '%s';"
            rows = self.cursor.execute(SELCT_IF_EXIST % (tb_common, url))
            if rows == 0:
                sql = "insert into scrape_yy(url, title, scrape_date, web_src) values(%s, %s, %s, %s)"
                self.cursor.execute(sql, (url, title, scrape_date, web_src))

            rows = self.cursor.execute(SELCT_IF_EXIST % (tb_common, url))
            if rows == 0:
                sql = "insert into yylive_news(url, title, scrape_date, web_src) values(%s, %s, %s, %s)"
                self.cursor.execute(sql, (url, title, scrape_date, web_src))

            self.conn.commit()

        except MySQLdb.Error, e:
            print "error %d: %s" % (e.args[0], e.args[1])

    # def insert(self):
    #     try:
    #         url = 'www.test.com'
    #         title = '女主播的故事'
    #         scrape_date = '2016-11-18 18:10:00'
    #
    #         sql = "insert into scrape_yy(url, title, scrape_date) values(%s, %s, %s)"
    #         self.cursor.execute(sql, (url, title, scrape_date))
    #         self.conn.commit()
    #
    #     except MySQLdb.Error, e:
    #         print "error %d: %s" % (e.args[0], e.args[1])

if __name__ == '__main__':
    my = MysqlPipeline()
    my.query()