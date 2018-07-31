# -*- coding: utf-8 -*-
#
# @Time    : 30/07/2018 17:17
#
# @Author  : WANG Wenxiao
#
# @FileName: img_scrape_lib.py
#

from common.my_urllib import *
import re
from os import chdir
from os import mkdir
import ssl

def download_all_img():
    imgpath = '/Users/shitong/Pictures/spyder/'
    url = input("输入网址：")
    ssl._create_default_https_context = ssl._create_unverified_context
    html = get_html(url).read().decode("UTF-8")
    bsObj = get_soup(html)
    print(bsObj.prettify())


if __name__ == "__main__":
    download_all_img()






