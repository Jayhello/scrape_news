# _*_ coding : utf-8 _*_

from scrapy.spider import CrawlSpider
from scrapy.selector import Selector
from utils.Json2XPath import Json2XPath, XPath
from scrape_yy.items import ScrapeYyItem
from utils.date import *
from utils.stringreg import get_absolute_url
from utils.log import get_logger
from scrapy import signals
from scrapy.mail import MailSender
import json


class CommonSpider(CrawlSpider):
    """
    This class is the base template class, which realize the real scrape function,
    if you want to scrape a new web just inherit it, and specify some parameters
    and the xpath.see one of the class in the directory "spiders" for example.
    """
    path = '../config/logging.json'
    logger = get_logger(path)

    def __init__(self, **kw):
        # CrawlSpider.__init__(self)
        jsonfile = kw['config']
        self.xp = Json2XPath(jsonfile).get_xpath()
        super(CommonSpider, self).__init__()
        self.need_send_mail = False
        self.mail_info = ''

    def parse(self, response):
        selector = Selector(response)
        articles = selector.xpath(self.xp.get_article())

        count = 0
        for article in articles:
            title = article.xpath(self.xp.get_xptitle()).extract()
            url = article.xpath(self.xp.get_xpurl()).extract()
            date = [None] * len(url)

            if self.xp.get_xptime():
                date = article.xpath(self.xp.get_xptime()).extract()

            for d, t, u in zip(date, title, url):
                item = ScrapeYyItem()
                item['title'] = t.strip()
                item['url'] = get_absolute_url(self.xp.get_name(), self.xp.get_url(), u).strip()
                item['url_date'] = d
                item['scrape_date'] = getNow()
                item['web_src'] = self.xp.get_name()
                item['webname'] = self.xp.get_webname()
                item['webtype'] = self.xp.get_webtype()
                # get the news source url like qq.com, news.163.com
                item['web_src_url'] = self.xp.get_url()

                count += 1
                print t, item['url']
                yield item

        # print 'scrape from %s get: %d' %(self.xp.get_name(), count)
        CommonSpider.logger.warn('scrape from %s get: %d' % (self.xp.get_name(), count))
        if count == 0:
            self.need_send_mail = True
            self.mail_info = 'scrape from %s get: %d news,maybe html structure change' % (self.xp.get_name(), count)

    @classmethod
    def from_crawler(cls, crawler):
        spider = cls()
        crawler.signals.connect(spider.spider_closed, signals.spider_closed)
        return spider

    def spider_closed(self, spider):
        # if some web can't be scraped, then send an email to acknowledge.
        if self.need_send_mail:
            CommonSpider.logger.warn(self.mail_info)

            jsonfile = '../config/mail.json'
            with open(jsonfile) as json_file_data:
                data = json.load(json_file_data)

            mf = data['mailfrom']
            smtphost = data['smtphost'].encode('utf-8')
            smtpport = data['smtpport']
            smtpuser = data['smtpuser'].encode('utf-8')
            smtppass = data['smtppass'].encode('utf-8')
            to = data['to'].encode('utf-8')
            subject = data['subject'].encode('utf-8')
            mailer = MailSender(mailfrom=mf, smtphost=smtphost,smtpport=smtpport,smtpuser=smtpuser,smtppass=smtppass)
            return mailer.send(to=to,subject=subject,body=self.mail_info)
