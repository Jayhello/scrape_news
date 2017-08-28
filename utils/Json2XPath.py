# _*_coding : utf-8
import json
from utils.config_str import *


class XPath:
    def __init__(self, url, name, article, webname,
                 webtype, xpath_title, xpath_url, xpath_time):
        self.url = url
        self.name = name
        self.article = article
        self.webname = webname
        self.webtype = webtype
        self.xpath_title = xpath_title
        self.xpath_url = xpath_url
        self.xpath_time = xpath_time

    def __str__(self):
        return 'url:%s, article:%s, xpath_title:%s, xpath_url:%s, xpath_time:%s' \
               % (self.url, self.article, self.xpath_title, self.xpath_url, self.xpath_time)

    def get_url(self):
        return self.url

    def get_name(self):
        return self.name

    def get_webname(self):
        return self.webname

    def get_webtype(self):
        return self.webtype

    def get_article(self):
        return self.article

    def get_xptitle(self):
        return self.xpath_title

    def get_xpurl(self):
        return self.xpath_url

    def get_xptime(self):
        return self.xpath_time


class Json2XPath:
    def __init__(self, jsonfile):
        with open(jsonfile) as json_file_data:
            data = json.load(json_file_data)

        url = data[URL]
        name = data[NAME]
        article = data[XPATH][ARTICLE]
        webname = data[WEBNAME]
        webtype = data[WEBTYPE]
        xpath_title = data[XPATH][XPATH_TITLE]
        xpath_url = data[XPATH][XPATH_URL]
        xpath_time = data[XPATH][XPATH_TIME]

        self.xp = XPath(url, name, article, webname, webtype, xpath_title, xpath_url, xpath_time)

    def __str__(self):
        return str(self.xp)

    def get_xpath(self):
        return self.xp


if __name__ == '__main__':

    path = '../scrape_yy/config/junjie.json'
    xp = Json2XPath(path).get_xpath()
    pass
    # print xp.get_url(), xp.get_article(), xp.get_name()
    # print "Current working directory is %s" % os.getcwd()
    # print os.path.join('H', 'work', 'lib')
    # print os.path.abspath("mydir/myfile.txt")
    # print os.path.abspath("")
    # print os.path.abspath("../")
    # import sys
    # print(sys.path)
    # sjson = '{"xpath_title":"a/text()","xpath_url":"a/@href", "article":"//div[@class=\\"lann\\"]/ul/li"}'
    # print json.loads(sjson)
