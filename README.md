﻿# 剑指offer
- python 刷题，希望有好结果
- 下面是解题思路

> 第32题，把数组排成最小的数并拼接起来，思路是把两个数字转为字符串并拼接，如比较3 和 31 则 变为比较 ‘331’ 和‘313’ ，再转为数字即可进行比较。因此定义一个cmp 比较函数，利用functools的cmp_to_key函数即可进行排序。
 sorted(numbers, key = functools.cmp_to_key(self.cmp))


> 第39题，判断是否为平衡二叉树。容易想到的方法是从上往下，判断左右子树的高度差是否<=1，然后继续递归判断左右子树 
