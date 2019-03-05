# -*- coding:utf-8 -*-
"""
-------------------------------------------------
   File Name：     fourty_eight
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
    def  __init__(self):
        self.res = -100
    def Add(self, num1, num2):
        if num2 == 0:
            if num1 <= 0x7FFFFFFF:
                return num1
            else:
                return ~(num1 ^0xFFFFFFFF)
        else:
            sum = (num1 ^ num2)& 0xFFFFFFFF
            tmp = ((num1 & num2) << 1) & 0xFFFFFFFF

            return self.Add(sum, tmp)





xx = Solution()
print(xx.Add(5,7))
print(xx.res)
