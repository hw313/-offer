# -*- coding:utf-8 -*-
"""
-------------------------------------------------
   File Name：     fifty_one
   Description :
   Author :       huang wei
   date：          2019/3/5
-------------------------------------------------
   Change Activity:
                   2019/3/5:
-------------------------------------------------
"""
__author__ = 'huang wei'
map = {}
map['A'] = 10
map['B'] = 11
map['C'] = 12
map['D'] = 13
map['E'] = 14
map['F'] = 15
hh = list(range(0, 10))
hh = [str(xx) for xx in hh]
for item in hh:
    map[item] = hh.index(item)
print(map)

xx = '0xC460'
xx = xx[2:]
if not xx:
    print()

tmp = 0
carry = 1
for i in range(len(xx) - 1, -1, -1):
    tmp += map[xx[i]] * carry
    carry = carry * 16
print(tmp)
    #
