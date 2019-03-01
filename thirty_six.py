# -*- coding:utf-8 -*-
"""
-------------------------------------------------
   File Name：     thirty_six
   Description :
   Author :       huang wei
   date：          2019/3/1
-------------------------------------------------
   Change Activity:
                   2019/3/1:
-------------------------------------------------
"""
__author__ = 'huang wei'

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        # write code here
        res = None
        if not pHead1 or not pHead2:
            return res
        len_1, len_2 = self.get_length(pHead1), self.get_length(pHead2)
        if len_1 < len_2:
            pHead2 = self.walk_num(pHead2, len_2 - len_1)
        else:
            pHead1 = self.walk_num(pHead1, len_1 - len_2)
        while pHead1:
            if pHead1 == pHead2:
                return pHead1
            else:
                pHead1 = pHead1.next
                pHead2 = pHead2.next
        return res

    def get_length(self, pHead):
        cnt = 0
        while pHead:
            cnt += 1
            pHead = pHead.next
        return cnt

    def walk_num(self, pHead, num):
        for _ in range(num):
            pHead = pHead.next
        return pHead


