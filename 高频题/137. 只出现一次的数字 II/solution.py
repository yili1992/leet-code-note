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
        return (3 * sum(set(nums)) - sum(nums)) // 2


if __name__ == '__main__':
    solution = Solution()
    grid = [0,1,0,1,0,1,99]

    print(solution.singleNumber(grid))
