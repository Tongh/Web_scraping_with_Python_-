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

req = get_requests("http://en.wikipedia.org/wiki/Kevin_Bacon")
bsObj = get_soup(req=req)

# with open("Kevin_Bacon", "w") as file:
#     file.write(bsObj.prettify())
num = 0
for link in bsObj.find("div", {"id": "bodyContent"}).findAll('a', href=re.compile("^(/wiki/)((?!:).)*$")):
    if 'href' in link.attrs:
        print(link.attrs['href'])
        num += 1

print(num)
