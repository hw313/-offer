# -*- coding:utf-8 -*-
"""
-------------------------------------------------
   File Name：     thirty_two
   Description :
   Author :       huang wei
   date：          2019/3/1
-------------------------------------------------
   Change Activity:
                   2019/3/1:
-------------------------------------------------
"""
__author__ = 'huang wei'
import functools


class Solution:
    def PrintMinNumber(self, numbers):
        numbers = sorted(numbers, key = functools.cmp_to_key(self.cmp))
        return "".join([str(item) for item in numbers])

    def cmp(self,a,b):
        a, b = str(a), str(b)
        if int(a+b) < int(b+a):
            return -1
        elif int(a+b) > int(b+a):
            return 1
        else:
            return 0

xx = Solution()
print(xx.PrintMinNumber([3,32,123,4,11]))