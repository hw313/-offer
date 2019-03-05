# -*- coding:utf-8 -*-
"""
-------------------------------------------------
   File Name：     thirty_three
   Description :
   Author :       huang wei
   date：          2019/3/5
-------------------------------------------------
   Change Activity:
                   2019/3/5:
-------------------------------------------------
"""
__author__ = 'huang wei'

class Solution:
    def GetUglyNumber_Solution(self, index):
        if index <= 6:
            return index
        res = [1]
        i, j, k =0, 0, 0
        while len(res) != index:
            tmp = min(res[i] * 2, res[j] * 3 ,res[k] * 5)
            res.append(tmp)
            if len(res) == index:
                return res[-1]
            if tmp == res[i] * 2:
                i += 1
            if tmp == res[j] * 3:
                j += 1
            if tmp == res[k] * 5:
                k += 1

import functools
import time
i = 1
def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print("call: {}".format(func.__name__))
        return func(*args, **kw)
    return wrapper

@log

def call():
    print(time.localtime())

call()