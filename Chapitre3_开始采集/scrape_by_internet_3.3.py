# -*- coding: utf-8 -*-
#
# @Time    : 31/07/2018 18:38
#
# @Author  : WANG Wenxiao
#
# @FileName: scrape_by_internet_3.3.py
#

from common.my_urllib import get_soup
from common.my_urllib import get_requests
from urllib.parse import urlparse
import re
import datetime
import random

pages = set()
random.seed(datetime.datetime.now())

def getInternalLinks(bsObj, includeURL):
    includeURL = urlparse(includeURL).scheme + "://" + urlparse(includeURL).netloc
    internalLinks = []
    for link in bsObj.findAll("a", href=re.compile("^(/|.*" + includeURL + ")")):
        if link.attrs['href'] not in internalLinks:
            if (link.attrs['href'].startswith("/")):
                internalLinks.append(includeURL + link.attrs['href'])
            else:
                internalLinks.append(link.attrs['href'])
    return internalLinks

def getExternalLinks(bsObj, excludeURL):
    externalLinks = []
    for link in bsObj.findAll("a", href=re.compile("^(http|www)((?!" + excludeURL + ").)*$")):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in externalLinks:
                externalLinks.append(link.attrs['href'])
    return externalLinks

def splitAddress(address):
    addressParts = address.replace("http://", "").split("/")
    return addressParts

def getRandomExternallink(startingPage):
    req = get_requests(startingPage)
    bsObj = get_soup(req=req)
    externalLinks = getExternalLinks(bsObj, urlparse(startingPage).netloc)
    if len(externalLinks) == 0:
        print("No external links, looking around the site for one")
        domain = urlparse(startingPage).scheme + "://" + urlparse(startingPage).netloc
        internalLinks = getInternalLinks(bsObj, domain)
        if len(internalLinks) == 0:
            print("Scrape end")
            return
        return getRandomExternallink(internalLinks[random.randint(0, len(internalLinks) - 1)])
    else:
        return externalLinks[random.randint(0, len(externalLinks) - 1)]

def followExternalOnly(startingSite):
    externalLink = getRandomExternallink(startingSite)
    if externalLink is None:
        return
    print("Random external link is " + externalLink)
    followExternalOnly(externalLink)

followExternalOnly("http://oreilly.com")