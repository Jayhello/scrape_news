# _*_ coding : utf-8

import time
import datetime


def getNow():
    """
    print (time.strftime("%Y-%m-%d %H:%M:%S"))
    print type(time.strftime("%Y-%m-%d %H:%M:%S"))
    type(time.strftime("%Y-%m-%d %H:%M:%S"))  => str
    :return like 2017-02-21 16:12:22:
    """
    return time.strftime("%Y-%m-%d %H:%M:%S")


def isJunJieToday(str_date):
    """
    str_date like '01.02.2017' , '12.22.2016'
    :return: true or false if str_date is today
    """
    dmy = [int(s) for s in str_date.split('.')]
    jjd, jjm, jjy = dmy[0], dmy[1], dmy[2]
    d, m, y = getYMD()

    return jjd == d and jjm == m and jjy == y


def getYMD():
    """
    :return year, month, day: like 2017 2 21 (int)
    """
    i = datetime.datetime.now()
    return i.day, i.month,i.year


def test_datetime():
    i = datetime.datetime.now()
    print ("Current date & time = %s" % i)
    print ("dd/mm/yyyy format =  %s/%s/%s" % (i.day, i.month, i.year) )
    print ("hh:mm:ss format = %s:%s:%s" % (i.hour, i.month, i.second) )
    print type(i)
    print i.strftime('%Y/%m/%d %H:%M:%S')
    print type(i.strftime('%Y/%m/%d %H:%M:%S'))

if __name__ == '__main__':
    print isJunJieToday('01.02.2017')
    print isJunJieToday('21.02.2017')
    print isJunJieToday('1.2.2017')
    # y, m, d = getYMD()
    # print type(m)
    # print m
    # print '01.02.2017'.split('.')
    # print [int(s) for s in '01.02.2017'.split('.')]
    # getNow()
    # test_datetime()
    ## 24 hour format ##
    # print (time.strftime("%H:%M:%S"))
    ## 12 hour format ##
    # print (time.strftime("%I:%M:%S"))

    ## dd/mm/yyyy format
    # print (time.strftime("%d.%m.%Y"))
    # print (time.strftime("%d.%m.%Y-%H:%M:%S"))
    # s = '02'
    # print int(s)
    # print "Current date & time " + time.strftime("%c")

    ## Only date representation
    # print "Current date "  + time.strftime("%x")

    ## Only time representation
    # print "Current time " + time.strftime("%X")

