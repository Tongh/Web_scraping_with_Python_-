# -*- coding: utf-8 -*-
#
# @Time    : 31/07/2018 13:24
#
# @Author  : WANG Wenxiao
#
# @FileName: modifier_requests_head_12.2.1.py
#

import requests
from bs4 import BeautifulSoup

"""
    浏览器网络请求数据
    Host    https://www.google.com/
    Connection  keep-alive
    Accept  text/html, application/xhtml+xml, application/xml;q=0.9, image/webp, */*;q=0.8
    User-Agent  Mozilla/5.0 (Macintosh; Intel Mac Os X 10_9_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36
    Referrer    https://www.google.com/
    Accept-Encoding     gzip, deflate, sdch
    Accept-Language     en-US,en;q=0.8
"""

"""
    Python请求头：
    Accept-Encoding     identify
    User-Agent      Python-urllib/3.4
"""

session = requests.Session()
headers = {"User-Agent":"Mozilla/5.0 (iPhone; CPU iPhone OS 7_1_2 like Mac OS X) AppleWebKit/537.51.2 (KHTML, like Gecko) Version/7.0 Mobile/11D257 Safari/9537.53",
           "Accept": "text/html,application/xhtml+xml,application/xml;q = 0.9, image / webp, * / *;q = 0.8"
           }

url = "https://www.whatismybrowser.com/detect/what-http-headers-is-my-browser-sending"

req = session.get(url, headers=headers)
bsObj = BeautifulSoup(req.text, "lxml")
print(bsObj.find("table", {"class": "table-striped"}).get_text)