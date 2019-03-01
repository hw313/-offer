# -*- coding:utf-8 -*-
"""
-------------------------------------------------
   File Name：     thirty_nine
   Description :
   Author :       huang wei
   date：          2019/2/28
-------------------------------------------------
   Change Activity:
                   2019/2/28:
-------------------------------------------------
"""
__author__ = 'huang wei'

import numpy as np


class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        # write code here
        if matrix is None:
            return None
        rows, cols = len(matrix), len(matrix[0])
        res = []
        while len(matrix) > 0:
            res += matrix.pop(0)
            if len(matrix) == 0:
                break
            matrix = self.rotate(matrix)
        return res

    def rotate(self, matrix):

        rows, cols = len(matrix), len(matrix[0])
        res = []
        for j in range(cols - 1, -1, -1):
            hh = []
            for i in range(rows):
                hh.append(matrix[i][j])
            res.append(hh)
        return res


xx = Solution()
# matrix = (np.arange(16)+1).reshape((4,4)).tolist()
matrix = [[1]]
print(xx.printMatrix(matrix))