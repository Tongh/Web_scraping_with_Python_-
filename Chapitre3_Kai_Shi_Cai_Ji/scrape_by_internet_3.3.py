# -*- coding: utf-8 -*-
#
# @Time    : 31/07/2018 18:38
#
# @Author  : WANG Wenxiao
#
# @FileName: scrape_by_internet_3.3.py
#

from common.my_urllib import get_soup
from urllib.parse import urlparse
import re
import datetime
import random

pages = set()
random.seed(datetime.datetime.now())


def get_internal_links(bsObj, includeURL):
    includeURL = urlparse(includeURL).scheme + "://" + urlparse(includeURL).netloc
    internalLinks = []
    for link in bsObj.findAll("a", href=re.compile("^(/|.*" + includeURL + ")")):
        if link.attrs['href'] not in internalLinks:
            if (link.attrs['href'].startswith("/")):
                internalLinks.append(includeURL + link.attrs['href'])
            else:
                internalLinks.append(link.attrs['href'])
    return internalLinks


def get_external_links(bsObj, excludeURL):
    externalLinks = []
    for link in bsObj.findAll("a", href=re.compile("^(http|www)((?!" + excludeURL + ").)*$")):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in externalLinks:
                externalLinks.append(link.attrs['href'])
    return externalLinks


def split_address(address):
    addressParts = address.replace("http://", "").split("/")
    return addressParts


def get_random_externallink(startingPage):
    bsObj = get_soup(startingPage)
    externalLinks = get_external_links(bsObj, urlparse(startingPage).netloc)
    if len(externalLinks) == 0:
        print("No external links, looking around the site for one")
        domain = urlparse(startingPage).scheme + "://" + urlparse(startingPage).netloc
        internalLinks = get_internal_links(bsObj, domain)
        if len(internalLinks) == 0:
            print("No internal links! End script")
            return
        return get_random_externallink(internalLinks[random.randint(0, len(internalLinks) - 1)])
    else:
        return externalLinks[random.randint(0, len(externalLinks) - 1)]


def follow_external_only(startingSite):
    externalLink = get_random_externallink(startingSite)
    if externalLink is None:
        return
    print("-" * 50)
    print("From", startingSite)
    print("Random external link is " + externalLink)
    follow_external_only(externalLink)


all_ext_links = set()
all_int_links = set()
def get_all_external_links(site_url):
    bsObj = get_soup(site_url)
    internal_links = get_internal_links(bsObj, split_address(site_url)[0])
    external_links = get_external_links(bsObj, split_address(site_url)[0])
    for link in external_links:
        if link not in all_ext_links:
            all_ext_links.add(link)
            print(link)
    for link in internal_links:
        if link not in all_int_links:
            print("即将获取的链接的url是:", link)
            all_int_links.add(link)
            get_all_external_links(link)


#follow_external_only("http://oreilly.com")
get_all_external_links("http://oreilly.com")


"""
    处理网页重定向
    重定向(redirect)允许一个网页在不同的域名下显示。重定向有两种形式:
    • 服务器端重定向，网页在加载之前先改变了 URL;
    • 客户端重定向，有时你会在网页上看到“10 秒钟后页面自动跳转到......”之类的消息，
    表示在跳转到新 URL 之前网页需要加载内容。 本节处理的是服务器端重定向的内容。更多关于客户端重定向的细节，通常用
    JavaScript 或 HTML 来实现，请看第 10 章。
    服务器端重定向，你通常不用担心。如果你在用 Python 3.x 版本的 urllib 库，它会自 动处理重定向。
    不过要注意，有时候你要采集的页面的 URL 可能并不是你当前所在页 面的 URL。
"""