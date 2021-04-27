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
    def medianSlidingWindow(self, nums, k: int):
        result = []
        def _get_median(n_l):
            if len(n_l) % 2 == 1:
                return n_l[len(n_l)//2]
            else:
                return (n_l[len(n_l) // 2] + n_l[len(n_l) // 2 - 1])/2
        a = sorted(nums[:k])
        result.append(_get_median(a))
        for i in range(k, len(nums)):
            a.remove(nums[i-k])
            bisect.insort_left(a, nums[i])
            result.append(_get_median(a))
        return result


if __name__ == '__main__':
    solution = Solution()
    nums = [1,3,-1,-3,5,3,6,7]
    k = 3
    result = solution.medianSlidingWindow(nums, k)
    print(result)
