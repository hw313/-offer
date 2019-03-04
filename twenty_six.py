# -*- coding:utf-8 -*-
"""
-------------------------------------------------
   File Name：     twenty_six
   Description :
   Author :       huang wei
   date：          2019/3/4
-------------------------------------------------
   Change Activity:
                   2019/3/4:
-------------------------------------------------
"""
__author__ = 'huang wei'
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def __init__(self):
        self.hehe = []

    def Convert(self, pRootOfTree):
        self.mid_order(pRootOfTree)
        for i in range(len(self.hehe)-1):
            self.hehe[i].right = self.hehe[i+1]
            self.hehe[i+1].left = self.hehe[i]

    def mid_order(self,Root):
        if root is None:
            return
        self.mid_order(Root.left)
        self.hehe.append(Root)
        self.mid_order(Root.right)
