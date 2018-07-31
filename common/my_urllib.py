# -*- coding: utf-8 -*-
#
# @Time    : 30/07/2018 16:45
#
# @Author  : WANG Wenxiao
#
# @FileName: my_urllib.py
#

import requests
from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
from bs4 import BeautifulSoup
import ssl
ssl._create_default_https_context = ssl._create_unverified_context


def get_requests(url, session=None, head=None):
    if session is None:
        session = requests.Session()
    if head is None:
        headers = {
            "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 7_1_2 like Mac OS X) AppleWebKit/537.51.2 (KHTML, like Gecko) Version/7.0 Mobile/11D257 Safari/9537.53",
            #'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36(KHTML, like Gecko) Chrome/38.0.2125.122 Safari/537.36 SE 2.X MetaSr 1.0',
            "Accept": "text/html, application/xhtml+xml, application/xml;q=0.9, image/webp, */*;q=0.8"
            }
    else:
        headers = head
    req = session.get(url, headers=headers)
    return req

def get_html(url):
    try:
        html = urlopen(url)
    except (HTTPError, URLError) as e:
        print("URLError reason:", e.reason)
        return None
    return html

def get_soup(url = None, html = None, parse="lxml", req=None):
    if html is None:
        if req is None:
            if url is None:
                print("Warning: get_soup() parameters are None")
                return None
            else:
                html = get_html(url).read()
        else:
            html = req.text
    bsObj = BeautifulSoup(html, parse)
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
