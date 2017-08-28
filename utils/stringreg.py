# -*- coding: utf-8 -*-
import random
import string


def str_related(title, webtype):
    """
    Check the new title contains certain keyword.
    if you want to search the title contains '直播', or '网络举报'
    you can set the keywords as below
    :param s a string like '......' :
    :return true if s contains keywords:
    """
    keywords = ['直播', '网络举报']

    if contains_keyword(title, keywords):
        return True

    # process gov web type particularly
    if webtype == 'gov':
        web_type_keywords = ['互联网信息', '网络举报', '有效举报', '网络违法',
                             '不良信息', '网络谣言', '互联网', '网络']
        if contains_keyword(title, web_type_keywords):
            return True

    return False


def contains_keyword(sentence, lst_keyword):
    """check if a sentence contains any keyword in keyword list"""
    for word in lst_keyword:
        word = word.lower()
        if sentence.find(word) >= 0:
            return True

    return False


def get_absolute_url(name, baseurl, url):
    """
    :param  url like /news/2017/03/31/484204.html
            baseurl like http://www.backchina.com/news/
    :return: like http://www.backchina.com/news/2017/03/31/484204.html
    """
    ret_url = url
    if name == 'junjie':
        ret_url = baseurl + url[url.rfind('/') + 1: len(url)]
    elif name == 'ccm_gov':
        ret_url = baseurl[0:baseurl.rfind('/')] + url[url.rfind('/'): len(url)]
    elif name == 'shdf':
        ret_url = baseurl[0:baseurl.find('/shdf')] + url
    elif name == 'myzaker' and url[0:2] == '//':
        ret_url = url[url.find('www'):]
    elif name == 'sootoo' and url.find('www') == -1:
        # http://www.sootoo.com/keyword/1520/
        # /content/670432.shtml  http://www.sootoo.com/content/670432.shtml
        ret_url = baseurl[0:baseurl.find('/keyword')] + url
    elif name == 'china_z' and url.find('www') == -1:
        # some like url = /news/2017/0330/681177.shtml
        # baseurl is http://www.chinaz.com/news/roll/
        # the final result is http://www.chinaz.com/news/2017/0330/681177.shtml
        ret_url = baseurl[0:baseurl.find('/news')] + url
    elif name == 'backchina' and url.find('www') == -1:
        # some like url = /news/2017/03/31/484204.html, or news/2017/03/31/484219.html
        # baseurl is http://www.backchina.com/news/
        # the final result is http://www.backchina.com/news/2017/03/31/484204.html
        if url.find('/news') == -1 and url.find('news') >= 0:
            ret_url = baseurl[0:baseurl.find('news')] + url
        else:
            ret_url = baseurl[0:baseurl.find('/news')] + url
    elif name == 'newspark' and url.find('www') == -1:
        # some like url = index.php?app=news&act=view&nid=226397
        # baseurl is http://news.6park.com/newspark/index.php
        # the final result is http://news.6park.com/newspark/index.php?app=news&act=view&nid=226397
        ret_url = baseurl[0:baseurl.find('index')] + url
    elif name == 'chinaso_network':
        # this website url is encrypted like below so we just return baseurl
        # url like this u'/stat/a.html?url=8E4A912C54052FC5C8.....'
        # as to save it to mysql and can be searched by scrape_search_yy we generate a 302 404 url, like
        # baseurl like http://news.chinaso.com/new/hulianwang/index.html
        # http://news.chinaso.com/new/hulianwang/you can't find this 123123123123/index.html
        # http://news.chinaso.com/new/hulianwang/you can't find this nums/index.html
        ret_url = baseurl[0:baseurl.find('index')] + generate_random_num_str(10) + '/index.html'
    elif name == 'news_youth' and url.find('www') == -1:
        # baseurl is http://news.youth.cn/sh/
        # url like ./201704/t20170401_9401911.htm
        # final url is http://news.youth.cn/sh/201704/t20170401_9401911.htm
        ret_url = baseurl + url[2:]
    elif name == 'mcprc' and url.find('www') == -1:
        # baseurl is http://www.mcprc.gov.cn/whzx/whyw/index.html
        # url like ./201704/t20170401_492855.html
        # final url is http://www.mcprc.gov.cn/whzx/whyw/201704/t20170401_492855.html
        ret_url = baseurl[:baseurl.find('index')] + url[2:]
    elif name == 'newarea' and url.find('www') == -1:
        # baseurl is http://district.ce.cn/newarea/zsyz/
        # url like ../roll/201704/06/t20170406_21751151.shtml
        # final url is http://district.ce.cn/newarea/roll/201704/06/t20170406_21751151.shtml
        ret_url = baseurl[:baseurl.find('zsyz')] + url[3:]
    elif name == 'legaldaily' and url.find('www') == -1:
        # baseurl is http://www.legaldaily.com.cn/node_20908.htm
        # url like index/content/2017-04/06/content_7081187.htm?node=20908
        # final url is http://www.legaldaily.com.cn/index/content/2017-04/06/content_7081494.htm?node=20908
        ret_url = baseurl[:baseurl.find('node')] + url
    elif name == 'ycwb' and url.find('www') == -1:
        # baseurl is http://news.ycwb.com/n_gd_jd.htm
        # url like 2017-04/06/content_24587180.htm
        # final url is http://news.ycwb.com/2017-04/06/content_24587180.htm
        ret_url = baseurl[:baseurl.find('n_gd')] + url

    return ret_url


def generate_random_num_str(length):
    """
    :param length:generated string length
    :return: random str from a-z and A-Z
    """
    return ''.join(random.choice(string.letters) for i in range(length))

if __name__ == '__main__':
    s1 = '主播直播时撕紧身裤 经纪人:再撕就斗鱼播了'
    s2 = '经纪人:再撕就不女主播播了'
    s3 = '经纪人:再撕就不让互联网播了'
    print str_related(s1, 'gov')
    print str_related(s2, 'gov')
    print str_related(s3, 'gov')

    # s = '/hulianwang/44760.html/123123.com'
    # print s[s.rfind('/') + 1: len(s)]