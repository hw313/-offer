# -*- coding:utf-8 -*-
"""
-------------------------------------------------
   File Name：     thirty_nine
   Description :
   Author :       huang wei
   date：          2019/3/1
-------------------------------------------------
   Change Activity:
                   2019/3/1:
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
        self.max_depth = -1
        self.depth = 0

    def IsBalanced_Solution(self, pRoot):
        if pRoot is None:
            return True
        left_depth = self.get_depth_parameter(pRoot.left)
        right_depth = self.get_depth_parameter(pRoot.right)
        if abs(left_depth-right_depth) > 1:
            return False
        return  self.IsBalanced_Solution(pRoot.left) and self.IsBalanced_Solution(pRoot.right)

    def get_depth_parameter(self,pRoot):
        self.__init__()
        # self.max_depth = -1
        # self.depth = 0
        return self.get_depth(pRoot)

    def get_depth(self, pRoot):


        if pRoot is None:
            return 0
        self.depth += 1
        if self.depth > self.max_depth:
            self.max_depth = self.depth
        self.get_depth(pRoot.left)
        self.get_depth(pRoot.right)
        self.depth -= 1
        return self.max_depth

def construct_tree():
    root = TreeNode(1)
    node1 = TreeNode(2)
    node2 = TreeNode(3)
    node3 = TreeNode(4)
    node4 = TreeNode(5)
    node5 = TreeNode(6)
    root.left, root.right = node1, node2
    node1.left, node1.right = node3, node4
    node4.left = node5
    node2.left = node2.right = node3.left = node3.right = node4.right = node5.left = node5.right = None
    return root

# root = construct_tree()
# xx = Solution()
# print(xx.IsBalanced_Solution(root))
# print(xx.get_depth_parameter(root))
# print(xx.get_depth_parameter(root.left))
# print(xx.get_depth_parameter(root.right))

def get_depth(root):
    if root is None:
        return  0
    return max(get_depth(root.left),get_depth(root.right))+1

# print(get_depth(root))
# print(get_depth(root.left))
# print(get_depth(root.right))


class Solve:
    def IsBalanced_Solution(self, p):
        return self.dfs(p) != -1
    def dfs(self, p):
        if p is None:
            return 0
        left = self.dfs(p.left)
        if left == -1:
            return -1
        right = self.dfs(p.right)
        if right == -1:
            return -1
        if abs(left - right) > 1:
            return -1
        return max(left, right) + 1
root = construct_tree()
xx = Solve()
print(xx.IsBalanced_Solution(root))