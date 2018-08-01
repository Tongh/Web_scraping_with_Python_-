# -*- coding: utf-8 -*-
#
# @Time    : 30/07/2018 17:17
#
# @Author  : WANG Wenxiao
#
# @FileName: img_scrape_lib.py
#

from common.my_urllib import get_soup
import re
from os import chdir
from os import mkdir
import ssl

def download_all_img(url):
    imgpath = '/Users/shitong/Pictures/spyder/'
    bsObj = get_soup(url)
    title = bsObj.title.get_text().strip()

if __name__ == "__main__":
    # https://mp.weixin.qq.com/s/biRIlYIiN2JvoP2amBYYkg
    url = input("输入网址：").strip()
    ssl._create_default_https_context = ssl._create_unverified_context
    download_all_img(url)






