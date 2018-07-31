# -*- coding: utf-8 -*-
#
# @Time    : 31/07/2018 12:29
#
# @Author  : WANG Wenxiao
#
# @FileName: ReWithBS2.4.py
#


from common.my_urllib import get_soup
import re

bsObj = get_soup("http://www.pythonscraping.com/pages/page3.html")

images = bsObj.findAll("img", {"src": re.compile("\.\.\/img\/gifts\/img.*\.jpg")})
for image in images:
    print(image, end="\t")
    print(image["src"])

"""
    2.5 获取属性
    到目前为止，我们已经介绍过如何获取和过滤标签，以及获取标签里的内容。
    但是，在网 络数据采集时你经常不需要查找标签的内容，而是需要查找标签属性。
    比如标签 <a> 指向 的 URL 链接包含在 href 属性中，或者 <img> 标签的图片文件包含在 src 属性中，这时获 取标签属性就变得非常有用了。
    对于一个标签对象，可以用下面的代码获取它的全部属性:
        myTag.attrs
    要注意这行代码返回的是一个 Python 字典对象，可以获取和操作这些属性。比如要获取图 片的资源位置 src，可以用下面这行代码:
        myImgTag.attrs["src"]
"""


"""
    2.6 Lambda 表达式
    Lambda 表达式本质上就是一个函数，可以作为其他函数的变量使用;
    也就是说，一个函 数不是定义成 f(x, y)，而是定义成 f(g(x), y)，或 f(g(x), h(x)) 的形式。
    
    BeautifulSoup 允许我们把特定函数类型当作 findAll 函数的参数。
    唯一的限制条件是这些 函数必须把一个标签作为参数且返回结果是布尔类型。
    BeautifulSoup 用这个函数来评估它 遇到的每个标签对象，最后把评估结果为“真”的标签保留，把其他标签剔除。
    
    例如，下面的代码就是获取有两个属性的标签:   
        soup.findAll(lambda tag: len(tag.attrs) == 2)
    这行代码会找出下面的标签:
        <div class="body" id="content"></div>
        <span style="color:red" class="title"></span>
"""