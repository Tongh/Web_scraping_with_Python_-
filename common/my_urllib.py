# -*- coding: utf-8 -*-
#
# @Time    : 30/07/2018 16:45
#
# @Author  : WANG Wenxiao
#
# @FileName: my_urllib.py
#

import requests
from bs4 import BeautifulSoup
import ssl
ssl._create_default_https_context = ssl._create_unverified_context


def get_requests(url, headers=None):
    if headers is None:
        headers = {
            "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 7_1_2 like Mac OS X) AppleWebKit/537.51.2 (KHTML, like Gecko) Version/7.0 Mobile/11D257 Safari/9537.53",
        # 手机端
            # 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36(KHTML, like Gecko) Chrome/38.0.2125.122 Safari/537.36 SE 2.X MetaSr 1.0',
            "Accept": "text/html, application/xhtml+xml, application/xml;q=0.9, image/webp, */*;q=0.8"}
    session = requests.Session()
    try:
        req = session.get(url, headers=headers)
    except BaseException as e:
        print("BaseException:", e.args)
        print("url:", url)
        return
    return req

def get_html(url, req = None):
    if req is None:
        req = get_requests(url)
    html = req.text
    return html

def get_soup(url = None, html = None, parse="lxml"):
    if html is None:
        if url is None:
            print("Warning: get_soup() parameters are None")
            return None
        else:
            html = get_html(url)
    bsObj = BeautifulSoup(html, parse)
    return bsObj

def get_title(url = None, html = None, bsObj = None):
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
