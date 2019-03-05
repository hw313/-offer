# -*- coding:utf-8 -*-
"""
-------------------------------------------------
   File Name：     thirty_five
   Description :
   Author :       huang wei
   date：          2019/3/5
-------------------------------------------------
   Change Activity:
                   2019/3/5:
-------------------------------------------------
"""
__author__ = 'huang wei'
import math


class Solution:
    def __init__(self):
        self.count = 0
    def InversePairs(self, arr):
        xx =self.merge_sort(arr)
        return self.count % 1000000007

    def merge_sort(self, arr):
        if len(arr) == 0 or len(arr) == 1:
            return arr
        start, end = 0, len(arr) - 1
        mid = math.ceil((start + end) / 2)
        left = self.merge_sort(arr[start:mid])
        right = self.merge_sort(arr[mid:])
        i, j, res = 0, 0, []
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                res.append(left[i])
                i += 1
            else:
                res.append(right[j])
                self.count += len(left) - i
                j += 1
        if i < len(left):
            res.extend(left[i:])
        if j < len(right):
            res.extend(right[j:])
        return res


xx = Solution()
a= xx.InversePairs([7,5,6,4])
print(a)
print(xx.count)


