#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: zhaoli01@corp.netease.com
@project: leet_code
@time: 2020-11-29 18:58
@desc:
"""


class Solution(object):
    def rotate(self, matrix: list) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n // 2):
            for j in range((n + 1) // 2):
                matrix[i][j], matrix[n - j - 1][i], matrix[n - i - 1][n - j - 1], matrix[j][n - i - 1] \
                    = matrix[n - j - 1][i], matrix[n - i - 1][n - j - 1], matrix[j][n - i - 1], matrix[i][j]
        return matrix

if __name__ == '__main__':
    solution = Solution()
    grid = [[5,1,9,11],
            [2,4,8,10],
            [13,3,6,7],
            [15,14,12,16]]
    print(solution.rotate(grid))  #  [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]