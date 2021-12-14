#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: zhaoli01@corp.netease.com
@project: leet_code
@time: 2020-11-29 18:58
@desc:
"""

class Solution(object):
    def singleNumber(self, nums) -> int:
        j = nums[0]
        for i in nums[1:]:
            j = j ^ i
            print(j)
        return j


if __name__ == '__main__':
    solution = Solution()
    grid = [4,1,2,1,2]

    print(solution.singleNumber(grid))

