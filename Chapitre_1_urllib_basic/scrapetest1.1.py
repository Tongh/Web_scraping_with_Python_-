# -*- coding: utf-8 -*-
#
# @Time    : 30/07/2018 16:01
#
# @Author  : WANG Wenxiao
#
# @FileName: scrapetest1.1.py
#

from urllib.request import urlopen
html = urlopen("http://pythonscraping.com/pages/page1.html")
print(html.read())

