# -*- coding: utf-8 -*-
#
# @Time    : 31/07/2018 12:03
#
# @Author  : WANG Wenxiao
#
# @FileName: NavigatingTreesTest2.2.3.py
#

from common.my_urllib import get_soup

bsObj = get_soup("http://www.pythonscraping.com/pages/page3.html")

print("处理子标签和其他后代标签")
for child in bsObj.find("table", {"id": "giftList"}).children:
    print(child)

"""
    这段代码会打印 giftList 表格中所有产品的数据行。
    如果你用 descendants() 函数而不是 children() 函数，那么就会有二十几个标签打印出来，
    包括 img 标签、span 标签，以及每 个 td 标签。掌握子标签与后代标签的差别十分重要!
"""

print("处理兄弟标签")
""" BeautifulSoup 的 next_siblings() 函数可以让收集表格数据成为简单的事情，尤其是处理 带标题行的表格 """

for sibling in bsObj.find("table", {"id": "giftList"}).tr.next_siblings:
    print(sibling)

"""
    这段代码会打印产品列表里的所有行的产品，第一行表格标题除外。
    为什么标题行被跳过 了呢?有两个理由。
    首先，对象不能把自己作为兄弟标签。
    任何时候你获取一个标签的兄弟标签，都不会包含这个标签本身。
    其次，这个函数只调用后面的兄弟标签。
    例如，如果 我们选择一组标签中位于中间位置的一个标签，然后用 next_siblings() 函数，那么它就 只会返回在它后面的兄弟标签。
    因此，选择标签行然后调用 next_siblings，可以选择表 格中除了标题行以外的所有行。
"""

"""
    让标签的选择更具体
    
    如果我们选择 bsObj.table.tr 或直接就用 bsObj.tr 来获取表格中的第一行， 上面的代码也可以获得正确的结果。
    但是，我们还是采用更长的形式写了一 行代码，这可以避免各种意外:
        bsObj.find("table",{"id":"giftList"}).tr
    即使页面上只有一个表格(或其他目标标签)，只用标签也很容易丢失细节。 
    另外，页面布局总是不断变化的。一个标签这次是在表格中第一行的位置， 没准儿哪天就在第二行或第三行了。
    如果想让你的爬虫更稳定，最好还是让 标签的选择更加具体。如果有属性，就利用标签的属性。
"""

"""
    和 next_siblings 一样，如果你很容易找到一组兄弟标签中的最后一个标签，那么 previous_siblings 函数也会很有用。
    当然，还有 next_sibling 和 previous_sibling 函数，与 next_siblings 和 previous_siblings 的作用类似，
    只是它们返回的是单个标签，而不是一组标签。
"""

print("父标签处理")
"""
    在抓取网页的时候，查找父标签的需求比查找子标签和兄弟标签要少很多。
    通常情况 下，如果以抓取网页内容为目的来观察 HTML 页面，我们都是从最上层标签开始的，然 后思考如何定位我们想要的数据块所在的位置。
    但是，偶尔在特殊情况下你也会用到 BeautifulSoup 的父标签查找函数，parent 和 parents。
"""

print(bsObj.find("img", {"src": "../img/gifts/img1.jpg"}).parent.previous_sibling.get_text())