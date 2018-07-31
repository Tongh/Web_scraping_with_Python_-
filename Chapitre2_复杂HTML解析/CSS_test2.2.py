# -*- coding: utf-8 -*-
#
# @Time    : 30/07/2018 16:44
#
# @Author  : WANG Wenxiao
#
# @FileName: CSS_test2.2.py
#

from common.my_urllib import *

bsObj = get_soup(url="http://www.pythonscraping.com/pages/warandpeace.html")

nameList = bsObj.findAll("span", {"class":"green"})
for name in nameList:
    print(name.get_text())
nameList = bsObj.findAll(text="the prince")
print(len(nameList))

"""
    findAll(tag, attributes, recursive, text, limit, keywords)
    find(tag, attributes, recursive, text, keywords)
        
        属性参数 attributes 是用一个 Python 字典封装一个标签的若干属性和对应的属性值。
             .findAll("span", {"class":{"green", "red"}})
        
        递归参数 recursive 是一个布尔变量。
            你想抓取 HTML 文档标签结构里多少层的信息?
            如果 recursive 设置为 True，findAll 就会根据你的要求去查找标签参数的所有子标签，以及子 标签的子标签。
            如果 recursive 设置为 False，findAll 就只查找文档的一级标签。
            findAll 默认是支持递归查找的(recursive 默认值是 True);
            一般情况下这个参数不需要设置，除非你真正了解自己需要哪些信息，而且抓取速度非常重要，那时你可以设置递归参数。
        
        文本参数 text 有点不同，它是用标签的文本内容去匹配，而不是用标签的属性。
            假如我们 想查找前面网页中包含“the prince”内容的标签数量，我们可以把之前的 findAll 方法换 成下面的代码:
                nameList = bsObj.findAll(text="the prince") 
                print(len(nameList))
            输出结果为“7”。
        
        范围限制参数 limit，显然只用于 findAll 方法。
            find 其实等价于 findAll 的 limit 等于 1 时的情形。
            如果你只对网页中获取的前 x 项结果感兴趣，就可以设置它。
            但是要注意，这个参数设置之后，获得的前几项结果是按照网页上的顺序排序的，未必是你想要的那前几项。
        
        还有一个关键词参数 keyword，可以让你选择那些具有指定属性的标签。例如: 
            allText = bsObj.findAll(id="text")
            print(allText[0].get_text())
"""
"""
    虽然关键词参数 keyword 在一些场景中很有用，但是，它是 BeautifulSoup 在 技术上做的一个冗余功能。
    任何用关键词参数能够完成的任务，同样可以用 本章后面将介绍的技术解决(请参见 2.3 节和 2.6 节)。
    例如，下面两行代码是完全一样的:
        bsObj.findAll(id="text")
        bsObj.findAll("", {"id":"text"})
    另外，用 keyword 偶尔会出现问题，尤其是在用 class 属性查找标签的时候， 因为 class 是 Python 中受保护的关键字。
    也就是说，class 是 Python 语言 的保留字，
    在 Python 程序里是不能当作变量或参数名使用的(和前面介绍 的 BeautifulSoup.findAll() 里的 keyword 无关)。
    假如你运行下面的代码， Python 就会因为你误用 class 保留字而产生一个语法错误:
        bsObj.findAll(class="green")
    不过，你可以用 BeautifulSoup 提供的有点儿臃肿的方案，在 class 后面增加一个下划线:
        bsObj.findAll(class_="green") 
    另外，你也可以用属性参数把 class 用引号包起来:
        bsObj.findAll("", {"class":"green"})
"""


