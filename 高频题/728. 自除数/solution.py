#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: zhaoli01@corp.netease.com
@project: leet_code
@time: 2020-11-29 18:58
@desc:
"""
import bisect

class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> list:
        result = []
        def _div_num(n):
            for j in str(n):
                if j == '0' or n % int(j) != 0:
                    return False
            return True

        for i in range(left, right+1):
            if _div_num(i):
                result.append(i)
        return result





if __name__ == '__main__':
    solution = Solution()
    left = 1
    right = 22
    # 输出： [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]
    result = solution.selfDividingNumbers(left, right)
    print(result)
