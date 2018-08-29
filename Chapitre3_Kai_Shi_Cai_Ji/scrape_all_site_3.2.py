# -*- coding: utf-8 -*-
#
# @Time    : 31/07/2018 16:01
#
# @Author  : WANG Wenxiao
#
# @FileName: scrape_all_site_3.2.py
#


from common.my_urllib import get_soup
from common.my_urllib import get_requests
import re

pages = set()

def get_links(pageURL):
    global pages
    req = get_requests("http://en.wikipedia.org" + pageURL)
    bsObj = get_soup(req=req)
    try:
        print(bsObj.h1.get_text())
        print(bsObj.find(id="mw-content-text").find("p"))
        print(bsObj.find(id="ca-edit").find("span").find("a").attrs['href'])
    except AttributeError as e:
        print("页面缺少一些属性！不过不用担心")

    for link in bsObj.findAll("a", href=re.compile("^(/wiki/)")):
        if "href" in link.attrs:
            if link.attrs["href"] not in pages:
                # 我们遇到了新页面
                newPage = link.attrs["href"]
                print("--------------------------\n" + newPage)
                pages.add(newPage)
                get_links(newPage)


get_links("")