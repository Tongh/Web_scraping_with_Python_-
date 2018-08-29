# -*- coding: utf-8 -*-
#
# @Time    : 31/07/2018 13:13
#
# @Author  : WANG Wenxiao
#
# @FileName: scrape_one_domaine3.1.py
#


from common.my_urllib import get_soup
from common.my_urllib import get_requests
import re
import datetime
import random

#req = get_requests("http://en.wikipedia.org/wiki/Kevin_Bacon")
#bsObj = get_soup(req=req)

# with open("Kevin_Bacon", "w") as file:
#     file.write(bsObj.prettify())

#for link in bsObj.find("div", {"id": "bodyContent"}).findAll('a', href=re.compile("^(/wiki/)((?!:).)*$")):
#    if 'href' in link.attrs:
#        print(link.attrs['href'])

def get_links(articleURL):
    req = get_requests("http://en.wikipedia.org" + articleURL)
    bsObj = get_soup(req=req, parse="html.parser")
    return bsObj.find("div", {"id": "bodyContent"}).findAll("a", href = re.compile("^(/wiki/)((?!:).)*$"))

links = get_links("/wiki/Kevin_Bacon")
while len(links) > 0:
    newArticle = links[random.randint(0, len(links) - 1)].attrs["href"]
    print(newArticle)
    links = get_links(newArticle)

