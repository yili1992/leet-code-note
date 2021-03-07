#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: zhaoli01@corp.netease.com
@project: leet_code
@time: 2020-11-29 18:58
@desc:
"""


class Solution:
    def partition(self, s: str):
        def helper(subStr):
            i, j = 0, len(subStr) - 1
            while i <= j:
                if subStr[i] != subStr[j]:
                    return False
                i += 1
                j -= 1
            return True

        def recall(s, size, start, subset):
            if start == size:
                res.append(subset[:])
                return
            for i in range(start, size):
                if not helper(s[start:i + 1]):
                    continue
                subset.append(s[start:i + 1])
                recall(s, size, i + 1, subset)
                subset.pop()

        res = []
        size = len(s)
        recall(s, size, 0, [])
        return res



if __name__ == '__main__':
    solution = Solution()
    print(solution.partition("aab"))