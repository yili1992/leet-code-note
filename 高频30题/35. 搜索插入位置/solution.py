#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: zhaoli01@corp.netease.com
@project: leet_code
@time: 2020-11-29 18:58
@desc:
"""


class Solution:
    def searchInsert(self, nums: list, target: int) -> int:
        if target > nums[-1]:
            return len(nums)
        if target <= nums[0]:
            return 0
        start = 0
        end = len(nums) -1
        while start < end:
            mid = (start + end)//2
            if target > nums[mid]:
                start = mid+1
            else:
                end = mid
        return end


if __name__ == '__main__':
    solution = Solution()
    grid, target = [1,3,5,7], 6
    print(solution.searchInsert(grid, target))