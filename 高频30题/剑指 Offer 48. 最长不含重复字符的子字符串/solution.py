#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: zhaoli01@corp.netease.com
@project: leet_code
@time: 2020-11-29 18:58
@desc:
"""


class Solution(object):
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        head = 0
        tail = 1
        max_len = 1
        while tail != len(s):
            if s[tail] not in s[head:tail]:
                tail += 1
                max_len = max(tail-head, max_len)
            else:
                head += 1
        return max_len


if __name__ == '__main__':
    solution = Solution()
    grid = "pwwkew"
    print(solution.lengthOfLongestSubstring(grid))