#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: zhaoli01@corp.netease.com
@project: leet_code
@time: 2020-11-29 18:58
@desc:
"""
import re


class Solution(object):
    max_value = 2 ** 31 - 1
    min_value = -2 ** 31
    def myAtoi(self, s: str) -> int:
        matcher = re.search(r'^[-|+]?\d+', s.strip())
        if matcher:
            result = int(matcher.group(0))
            if result > Solution.max_value:
                result = Solution.max_value
            if result < Solution.min_value:
                result = Solution.min_value
            return result
        else:
            return 0



if __name__ == '__main__':
    solution = Solution()
    grid = "+4193 words 193"
    print(solution.myAtoi(grid))