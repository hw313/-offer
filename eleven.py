# -*- coding:utf-8 -*-
"""
-------------------------------------------------
   File Name：     eleven
   Description :
   Author :       huang wei
   date：          2019/3/1
-------------------------------------------------
   Change Activity:
                   2019/3/1:
-------------------------------------------------
"""
__author__ = 'huang wei'

# 二进制

class Solution:
    def NumberOf1(self, n):
        if n == 0:
            return 0
        if n == -pow(2,31):
            return 1
        xx = self.convert2binary(n)
        print(xx)
        return xx.count(1)

    def convert2binary(self, n):
        if n > 0:
            res = []
            while n:
                res.append(n % 2)
                n =(n- n%2)/2
            res = res[::-1]
            return res
        else:
            symbol = [1]
            res = []
            n = -n
            while n:
                res.append(n % 2)
                n =(n- n%2)/2
            res = res[::-1]

            xx = [0] * (31 - len(res))
            xx += res
            xx= [1-x for x in xx]
            symbol += xx

            res = self.add_1(symbol)
            return res

    def add_1(self, array):
        add =[0] * (len(array) - 1)
        add += [1]
        carry = 0
        res = []
        for i in range(len(array)-1, -1, -1):
            temp = array[i] + add[i] + carry
            carry = int (temp / 2)
            res.append(temp % 2)
        if carry:
            res.append(1)

        return res[::-1]



xx = Solution()
print(xx.NumberOf1(-2147483648))


print(pow(2,31)-1)


class Solution:
    def NumberOf1(self, n):
        # write code here
        count = 0
        if n < 0:
            n = n & 0xffffffff
        while n:
            count += 1
            n = (n - 1) & n
        return count