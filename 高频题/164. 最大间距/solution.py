#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: zhaoli01@corp.netease.com
@project: leet_code
@time: 2020-11-29 18:58
@desc:
"""
from functools import reduce

class Solution:
    def maximumGap(self, nums):
        if len(nums) <2:
            return 0
        sort_l = sorted(nums)
        max_num = 0
        for i in range(1, len(sort_l)):
            max_num = max(sort_l[i]-sort_l[i-1], max_num)
        return max_num


if __name__ == '__main__':
    solution = Solution()
    a = [3,6,9,1]
    result = solution.maximumGap(a)
    print(result)
