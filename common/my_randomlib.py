# -*- coding: utf-8 -*-
#
# @Time    : 30/07/2018 17:20
#
# @Author  : WANG Wenxiao
#
# @FileName: my_randomlib.py
#


from datetime import *
import random


def get_random_unique_number(num=1):
    res = list()
    for i in range(num):
        nowTime = datetime.now().strftime("%Y%m%d%H%M%S")  # 生成当前的时间
        randomNum = random.randint(0, 100)  # 生成随机数n,其中0<=n<=100
        if randomNum <= 10:
            randomNum = str(0) + str(randomNum)
        uniqueNum = str(nowTime) + str(randomNum)
        if num == 1:
            return uniqueNum
        res.append(uniqueNum)
    return res