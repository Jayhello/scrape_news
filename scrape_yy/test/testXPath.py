# -*- coding: utf-8 -*-
from scrapy import Selector
from scrapy.http import HtmlResponse
import requests
import json

def test_xpath():
    html = u"""<!DOCTYPE html>
            <html>
            <head lang="en">
                <meta charset="UTF-8">
                <title></title>
            </head>
            <body>
                <li class="item-"><a href="link.html">first item</a></li>
                <li class="item-0"><a href="link1.html">first item</a></li>
                <li class="item-1"><a href="link2.html">second item</a></li>
                <span>foobar</span>

                <div class ="lann">
                    <ul>
                        <li>
                            <span class="date">12.13.2016</span>
                            <a target="_blank" href="/hulianwang/45345.html" title="西安空姐离职当网络主播半年吸粉33万 月入5万元">西安空姐离职当网络主播半年吸粉33万&nbsp;月入5万元</a>
                        </li>
                        <li>
                            <span class="date">1.13.2017</span>
                            <a target="_blank" href="/hulianwang/45345.html" title="西安空姐离职当网络主播半年吸粉33万 月入5万元">==================</a>
                        </li>
                    </ul>

                    <ul class="lannad">
                        <script>
                        </script>
                    </ul>
                </div>

                <div class ="tab active">
                    <li class="red">tab red 1111111111</li>
                    <li class="black">tab black li 1111111111</li>
                    <span class="date">1.13.2017</span>
                </div>

                <div class ="tab">
                    <span class="date">1.13.2017</span>
                </div>

                <div class ="tab active">
                    <td class="red">tab active red</td>
                    <span class="date">span active red</span>
                    <li class="red">tab red 2222222222</li>
                    <li class="black">tab black li 2222222222</li>
                </div>

                <div class ="test">
                    1.13.2017
                </div>
                <div class ="test abc">
                    test abc
                </div>
            </body>
            </html>
            """

    response = HtmlResponse(url='http://example.com', body=html, encoding='utf-8')
    # ret = Selector(response=response).xpath('//li[re:test(@class, "item-\d*")]//@href').extract()
    # ret = Selector(response=response).xpath('//div[@class="lann"]/ul/li/span/text()').extract()
    # ret = Selector(response=response).xpath('//div[@class="lann"]/ul/li')
    # ret1 = Selector(response=response).xpath('//div[@class="lann"]/ul/li/a/@title').extract()[0]
    xp = '//div[@class="tab"]/td[@class="red"]/text()'
    xp = '//div[@class="test abc"]/text()'
    xp = '//div[@class="tab active"]/td[@class="red"]/text()'
    xp = '//div[@class="tab active"]'
    # xp = '//li[@class="red"]/text()'
    selector = Selector(response)
    articles = selector.xpath(xp)
    for article in articles:
        # ti = 'td/text()'
        ti = 'li[@class="red"]/text()'
        s = article.xpath(ti).extract()[0]
        print s

    ret = Selector(response=response).xpath(xp).extract()
    return ret

def test_TG():
    html = u"""<!DOCTYPE html>
            <html>
            <head lang="en">
                <meta charset="UTF-8">
                <title></title>
            </head>
            <body>
                <div class ="lann">
                    <ul>
                        <li>
                            <span class="date">12.13.2016</span>
                            <a target="_blank" href="/hulianwang/45345.html" title="西安空姐离职当网络主播半年吸粉33万 月入5万元">西安空姐离职当网络主播半年吸粉33万&nbsp;月入5万元</a>
                        </li>
                        <li>
                            <span class="date">1.13.2017</span>
                            <a target="_blank" href="/hulianwang/45345.html" title="西安空姐离职当网络主播半年吸粉33万 月入5万元">==================</a>
                        </li>
                    </ul>

                    <ul>
                         <li>
                            <span class="date">12.13.2016</span>
                            <a target="_blank" href="/hulianwang/45345.html" title="西安空姐离职当网络主播半年吸粉33万 月入5万元">西安空姐离职当网络主播半年吸粉33万&nbsp;月入5万元</a>
                        </li>
                        <li>
                            <span class="date">1.13.2017</span>
                            <a target="_blank" href="/hulianwang/45345.html" title="西安空姐离职当网络主播半年吸粉33万 月入5万元">==================</a>
                        </li>
                    </ul>
                </div>

            </body>
            </html>
            """

    response = HtmlResponse(url='http://example.com', body=html, encoding='utf-8')
    xp = '//div[@class="lann"]/ul'
    selector = Selector(response)
    articles = selector.xpath(xp)

    for article in articles:
        # ti = 'td/text()'
        ti = 'li/a/text()'
        # s = article.xpath(ti).extract()[0]
        s = article.xpath(ti).extract()
        print s

    ret = Selector(response=response).xpath(xp).extract()
    return ret

def test_huanqiu():
    html = u"""<!DOCTYPE html>
            <html>
            <head lang="en">
                <meta charset="UTF-8">
                <title></title>
            </head>
            <body>
                <div class ="lann">
                    <span></span>
                    123
                       <ul>
                         <li>
                            <span class="date">12.13.2016</span>
                            <a target="_blank" href="/hulianwang/45345.html" title="西安空姐离职当网络主播半年吸粉33万 月入5万元">西安空姐离职当网络主播半年吸粉33万&nbsp;月入5万元</a>
                        </li>
                        <li>
                            <span class="date">1.13.2017</span>
                            <a target="_blank" href="/hulianwang/45345.html" title="西安空姐离职当网络主播半年吸粉33万 月入5万元">==================</a>
                        </li>
                    </ul>
                </div>

            </body>
            </html>
            """
    response = HtmlResponse(url='http://example.com', body=html, encoding='utf-8')
    xp = '//div[@class="lann"]/ul/li'
    selector = Selector(response)
    print selector.xpath(xp).extract()


def test_china():
    html = u"""<!DOCTYPE html>
            <html>
            <head lang="en">
                <meta charset="UTF-8">
                <title></title>
            </head>
            <body>
            <div class ="main">
                <div class ="left">
                       <ul>
                         <li>
                            <span class="date">12.13.2016</span>
                            <a target="_blank" href="/hulianwang/45345.html" title="西安空姐离职当网络主播半年吸粉33万 月入5万元">西安空姐离职当网络主播半年吸粉33万&nbsp;月入5万元</a>
                        </li>
                        <li>
                            <span class="date">1.13.2017</span>
                            <a target="_blank" href="/hulianwang/45345.html" title="西安空姐离职当网络主播半年吸粉33万 月入5万元">==================</a>
                        </li>
                    </ul>
                </div>
                <div class ="right">
                       <ul>
                         <li>
                            <span class="date">12.13.2016</span>
                            <a target="_blank" href="/hulianwang/45345.html" title="西安空姐离职当网络主播半年吸粉33万 月入5万元">西安空姐离职当网络主播半年吸粉33万&nbsp;月入5万元</a>
                        </li>
                        <li>
                            <span class="date">1.13.2017</span>
                            <a target="_blank" href="/hulianwang/45345.html" title="西安空姐离职当网络主播半年吸粉33万 月入5万元">==================</a>
                        </li>
                    </ul>
                </div>
            </div>
            </body>
            </html>
            """
    response = HtmlResponse(url='http://example.com', body=html, encoding='utf-8')
    xp = '//div[@class="main"]//ul'
    selector = Selector(response)
    articles = selector.xpath(xp)

    for article in articles:
        urls = article.xpath('li/a/@title').extract()
        for u in urls:
            print u


def test_shxwcb():
    html = u"""<!DOCTYPE html>
            <html>
            <head lang="en">
                <meta charset="UTF-8">
                <title></title>
            </head>
            <body>
            <div class ="main">
                <div class ="left" id="main">
                       <ul>
                         <li id="post-13275">
                            <span class="date">12.13.2016</span>
                            <a target="_blank" href="/hulianwang/45345.html" title="11西安空姐离职当网络主播半年吸粉33万 月入5万元">西安空姐离职当网络主播半年吸粉33万&nbsp;月入5万元</a>
                        </li>
                        <li id="post-1350">
                            <span class="date">1.13.2017</span>
                            <a target="_blank" href="/hulianwang/45345.html" title="1111西安空姐离职当网络主播半年吸粉33万 月入5万元">==================</a>
                        </li>
                    </ul>
                </div>
                <div class ="right">
                       <ul>
                         <li>
                            <span class="date">12.13.2016</span>
                            <a target="_blank" href="/hulianwang/45345.html" title="西安空姐离职当网络主播半年吸粉33万 月入5万元">西安空姐离职当网络主播半年吸粉33万&nbsp;月入5万元</a>
                        </li>
                        <li id="post-1350">
                            <span class="date">1.13.2017</span>
                            <a target="_blank" href="/hulianwang/45345.html" title="西安空姐离职当网络主播半年吸粉33万 月入5万元">==================</a>
                        </li>
                    </ul>
                </div>
            </div>
            </body>
            </html>
            """
    response = HtmlResponse(url='http://example.com', body=html, encoding='utf-8')
    xp = '//div[@id="main"]'
    selector = Selector(response)
    articles = selector.xpath(xp)

    for article in articles:
        urls = article.xpath('//li/a/@title').extract()
        for u in urls:
            print u

def test_sinapic():
    html = u"""<!DOCTYPE html>
            <html>
            <head lang="en">
                <meta charset="UTF-8">
                <title></title>
            </head>
            <body>
                <div class ="right">
                       <ul>
                         <li>
                            <span class="date">12.13.2016</span>
                            <a target="_blank" href="/hulianwang/45345.html" title="西安空姐离职当网络主播半年吸粉33万 月入5万元">西安空姐离职当网络主播半年吸粉33万&nbsp;月入5万元</a>
                        </li>
                        <li id="post-1350">
                            <span class="date">1.13.2017</span>
                            <a target="_blank" href="/hulianwang/45345.html" title="西安空姐离职当网络主播半年吸粉33万 月入5万元">==================</a>
                        </li>
                    </ul>
                </div>
            </div>
            </body>
            </html>
            """
    response = HtmlResponse(url='http://example.com', body=html, encoding='utf-8')
    xp = '//span[@class="date"]'
    selector = Selector(response)
    articles = selector.xpath(xp)

    for article in articles:
        urls = article.xpath('text()').extract()
        for u in urls:
            print u


if __name__ == '__main__':
    url = "http://localhost:8099"
    data = {'sender': 'Alice', 'receiver': 'Bob', 'message': 'We did it!'}
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    r = requests.post(url, data=json.dumps(data), headers=headers)
    # test_sinapic()
    # test_shxwcb()
    # test_china()
    # test_huanqiu()
    # test_TG()
    # print test_xpath()
    # a = [[]] * 5
    # a[0].append(0)
    # print a[0][0]
    # print [None for a in xrange(3)]



