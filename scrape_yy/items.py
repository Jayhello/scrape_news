# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Item, Field


class ScrapeYyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = Field()
    url = Field()
    url_date = Field()
    scrape_date = Field()
    web_src = Field()
    webname = Field()
    webtype = Field()
    web_src_url = Field()