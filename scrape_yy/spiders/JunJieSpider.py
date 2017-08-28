# _*_ coding : utf-8

from CommonSpider import CommonSpider


class JunJieSpider(CommonSpider):
    name = 'junjie'
    start_urls = ['http://www.junjiewang.com/hulianwang/']

    def __init__(self):
        super(JunJieSpider, self).__init__(config='config/junjie.json')