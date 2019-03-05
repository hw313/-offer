# -*- coding:utf-8 -*-
"""
-------------------------------------------------
   File Name：     thirty_one
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
    def NumberOf1Between1AndN_Solution(self, n):
        # write code here
        Str = ""
        for _ in range(1,n+1):
            Str += str(_)
        return Str.count('1')