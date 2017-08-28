# _*_ coding:utf-8 _*_

import os

from scrapy import cmdline
import json
import random
import time
from utils.log import get_logger


def get_log():
    path = '../config/logging.json'
    return get_logger(path)

logger = get_log()


def get_spider_list():
    jsonfile = 'run_config/scrape_list.json'
    with open(jsonfile) as json_file_data:
        data = json.load(json_file_data)

    ret_lst = [item.encode('utf-8') for item in data['scrape_list']]
    random.shuffle(ret_lst)
    return ret_lst


def do_scrape_task():
    web_list = get_spider_list()
    for web in web_list:
        logger.info('now scrape from %s:' % web)
        # start a new process to execute scrape, or the scrape process
        # will exit the process by default. There are some other ways to do
        # that but I found os.system is the simplest way.
        os.system('scrapy crawl %s' % web)


def run():
    while True:
        jsonfile = 'run_config/run_config.json'
        with open(jsonfile) as json_file_data:
            data = json.load(json_file_data)

        minute = data['minute']

        do_scrape_task()

        logger.warn('scrape all, now sleeping %d minutes' % minute)
        time.sleep(60 * minute)

if __name__ == '__main__':
    # scrape all the web in the file 'scrape_list.json'
    # run()

    # scrape one web once(the following scrape the website "neteasy")
    cmdline.execute('scrapy crawl neteasy'.split())
    # cmdline.execute('scrapy crawl junjie'.split())
    # cmdline.execute('scrapy crawl news21cn'.split())
    # cmdline.execute('scrapy crawl legaldaily'.split())
    # cmdline.execute('scrapy crawl newarea'.split())
    # cmdline.execute('scrapy crawl baidu'.split())
    # cmdline.execute('scrapy crawl tiexue'.split())
    # cmdline.execute('scrapy crawl backchina'.split())
    # cmdline.execute('scrapy crawl xinhua'.split())
    # cmdline.execute('scrapy crawl mcprc'.split())
    # cmdline.execute('scrapy crawl toutiao'.split())
    # cmdline.execute('scrapy crawl southcn_society'.split())
    # cmdline.execute('scrapy crawl news_youth'.split())
    # cmdline.execute('scrapy crawl chinaso_society'.split())
    # cmdline.execute('scrapy crawl chinaso_network'.split())
    # cmdline.execute('scrapy crawl tianya'.split())
    # cmdline.execute('scrapy crawl newspark'.split())
