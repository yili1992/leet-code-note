#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: zhaoli01@corp.netease.com
@project: leet_code
@time: 2020-11-29 18:58
@desc:
"""


class Solution:
    def findPeakElement(self, nums) -> int:
        head = 0
        if len(nums) == 1:
            return 0
        if len(nums) == 2:
            if nums[0] > nums[1]:
                return 0
            else:
                return 1
        for tail in range(2, len(nums)):
            if nums[head] < nums[head+1] and nums[head+1] > nums[tail]:
                break
            else:
                head += 1
        else:
            if nums[head] < nums[head+1]:
                return head + 1
            else:
                return 0

        return head+1

if __name__ == '__main__':
    solution = Solution()
    a = [1,2,3]
    result = solution.findPeakElement(a)
    print(result)
