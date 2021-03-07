#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: zhaoli01@corp.netease.com
@project: leet_code
@time: 2020-11-22 13:21
@desc:
"""


class Solution:
    def merge(self, nums1, m: int, nums2, n: int) -> list:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1.extend(nums2)
        nums1.sort()
        for i in range(n):
            nums1.remove(0)
        print(nums1)


if __name__ == '__main__':
    nums1 = [-1,0,0,3,3,3,0,0,0]
    m = 6
    nums2 = [1,2,2]
    n = 3
    solution = Solution()
    solution.merge(nums1, m, nums2, n)