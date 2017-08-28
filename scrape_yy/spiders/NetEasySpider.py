# _*_ coding : utf-8

from CommonSpider import CommonSpider


class NetEasySpider(CommonSpider):
    name = 'neteasy'
    start_urls = ['http://news.163.com/rank/']

    def __init__(self):
        super(NetEasySpider, self).__init__(config = 'config/neteasy.json')
