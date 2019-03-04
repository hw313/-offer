# -*- coding:utf-8 -*-
"""
-------------------------------------------------
   File Name：     twenty_five
   Description :
   Author :       huang wei
   date：          2019/3/3
-------------------------------------------------
   Change Activity:
                   2019/3/3:
-------------------------------------------------
"""
__author__ = 'huang wei'
# 复杂链表的复制

class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

    def __str__(self):
        return "它的值为{},下一个结点 {} ".format(self.label, self.next)


class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        if not pHead:
            return None
        p = root = pHead
        while pHead:
            new = RandomListNode(pHead.label)
            new.next = pHead.next
            pHead.next = new
            pHead = new.next

        while root and root.next:
            root_new = root.next
            if root.random:
                root_new.random = root.random.next
            else:
                root_new.random = None

            root = root.next.next

        # head =tmp =  p.next
        # while tmp and tmp.next:
        #     tmp.next = tmp.next.next
        #     tmp = tmp.next
        # tmp.next = None
        # return head


        dummy = p
        copyHead = p.next
        while dummy:
            copyNode = dummy.next
            dummynext = copyNode.next
            dummy.next = dummynext
            if dummynext:
                copyNode.next = dummynext.next
            else:
                copyNode.next = None
            dummy = dummynext

        return copyHead

def construct():
    a = RandomListNode(1)
    b = RandomListNode(2)
    c = RandomListNode(3)
    d = RandomListNode(4)
    e = RandomListNode(5)
    a.next = b
    b.next = c
    c.next = d
    d.next = e
    e.next = None
    a.random = c
    b.random = e
    d.random = b
    c.random = e.random = None
    return a

a = construct()
xx = Solution()
c = xx.Clone(a)
print(c.next.random)



