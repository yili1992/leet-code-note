#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: zhaoli01@corp.netease.com
@project: leet_code
@time: 2020-11-29 18:58
@desc:
"""


class Solution(object):
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0
        x_str = str(x)
        try:
            if x_str[0] == '-':
                result = int('-'+x_str[len(x_str):0:-1])
            else:
                result = int(x_str[::-1])
        except:
            result = 0
        if result > 2**31-1 or result < -2 ** 31:
            result = 0
        return result




if __name__ == '__main__':
    solution = Solution()
    grid = -129
    print(solution.reverse(grid))