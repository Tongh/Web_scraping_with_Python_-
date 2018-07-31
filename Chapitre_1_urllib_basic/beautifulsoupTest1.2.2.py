# -*- coding: utf-8 -*-
#
# @Time    : 30/07/2018 16:05
#
# @Author  : WANG Wenxiao
#
# @FileName: beautifulsoupTest1.2.2.py
#

from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen("http://www.pythonscraping.com/pages/page1.html")
bsObj = BeautifulSoup(html.read(), "lxml")
print(bsObj.h1)
print(bsObj.prettify())
