# -*- coding:utf-8 -*-
"""
-------------------------------------------------
   File Name：     twenty_seven
   Description :
   Author :       huang wei
   date：          2019/3/4
-------------------------------------------------
   Change Activity:
                   2019/3/4:
-------------------------------------------------
"""

# class Solution:
#     def __init__(self):
#         self.res = []
#
#     def Permutation(self, ss):
#         if not ss:
#             return []
#         elif len(ss) == 1 or len(ss) == 0:
#             return [ss]
#         else:
#             self.__init__()
#             for i in range(len(ss)):
#                 for j in self.Permutation(ss[:i]+ss[i+1:]):
#                     if ss[i]+j not in self.res:
#                         self.res.append(ss[i]+j)
#         return sorted(self.res)



class Solution:
    def Permutation(self, ss):
        # write code here
        if not ss:
            return []
        if len(ss) == 1:
            return [ss]
        ret = []
        #遍历字符串，固定第一个元素，然后递归求解
        for i in range(len(ss)):
            for j in self.Permutation(ss[:i]+ss[i+1:]):
                ret.append(ss[i]+j)
        #通过set进行去重，sorted进行重新排序
        return sorted(list(set(ret)))
xx = Solution()
print(xx.Permutation("abc"))