# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        # write code here
        flag = False
        if not pRoot2 or not pRoot1:
            return False
        if self.is_equal(pRoot1.left, pRoot2):
            flag = True
            return True
        elif self.is_equal(pRoot1.right, pRoot2):
            flag = True
            return True
        else:
            flag = self.HasSubtree(pRoot1.left, pRoot2)
            if not flag:
                flag = self.HasSubtree(pRoot1.right, pRoot2)
            return flag

    def is_equal(self, pRoot1, pRoot2):
        if pRoot2 == None:
            return True
        if pRoot1 == None:
            return False
        if pRoot1.val != pRoot2.val:
            return False
        else:
            return self.is_equal(pRoot1.left, pRoot2.left) and self.is_equal(pRoot1.right, pRoot2.right)