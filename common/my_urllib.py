# -*- coding: utf-8 -*-
#
# @Time    : 30/07/2018 16:45
#
# @Author  : WANG Wenxiao
#
# @FileName: my_urllib.py
#

from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
from bs4 import BeautifulSoup


def get_html(url):
    try:
        html = urlopen(url)
    except (HTTPError, URLError) as e:
        print("URLError reason:", e.reason)
        return None
    return html

def get_soup(url = None, html = None, parse="lxml"):
    if html is None:
        if url is None:
            print("Warning: get_soup() parameters are None")
            return None
        else:
            html = get_html(url)
    bsObj = BeautifulSoup(html.read(), parse)
    return bsObj

def get_title(url = None, html = None, bsObj=None):
    if bsObj is None:
        if html is None:
            if url is None:
                print("Warning: get_title() parameters are None")
                return None
            bsObj = get_soup(url)
        bsObj = get_soup(html)
    try:
        title = bsObj.title
    except AttributeError as e:
        print("This HTML has not title")
        return None
    return title
