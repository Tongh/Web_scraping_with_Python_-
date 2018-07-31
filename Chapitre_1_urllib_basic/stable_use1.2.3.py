# -*- coding: utf-8 -*-
#
# @Time    : 30/07/2018 16:18
#
# @Author  : WANG Wenxiao
#
# @FileName: stable_use1.2.3.py
#

from urllib.request import urlopen
from urllib.error import HTTPError, URLError
from bs4 import BeautifulSoup


try:
    html = urlopen("http://www.pythonscraping.com/pages/page1.html")
except HTTPError as e:
    print(e)
    # 返回空值，中断程序，或者执行另一个方案
else:
    # 程序继续。注意:如果你已经在上面异常捕捉那一段代码里返回或中断(break)， # 那么就不需要使用else语句了，这段代码也不会执行
    if html is None:
        print("URL is not found")
    else:
        bsObj = BeautifulSoup(html.read(), "lxml")
        try:
            badContent = bsObj.title
        except AttributeError as e:
            print("Tag was not found")
        else:
            if badContent == None:
                print("Tag was not found")
            else:
                print(badContent)


def getTitle(url):
    try:
        html = urlopen(url)
    except (HTTPError, URLError) as e:
        return None
    try:
        bsObj = BeautifulSoup(html.read(), 'lxml')
        title = bsObj.body.h1
    except AttributeError as e:
        return None
    return title
title = getTitle("http://www.pythonscraping.com/pages/page1.html")
if title == None:
    print("Title could not be found")
else:
    print(title)

