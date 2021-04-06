#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: zhaoli01@corp.netease.com
@project: leet_code
@time: 2020-11-29 18:58
@desc:
"""


class Solution:
    def longestCommonPrefix(self, strs) -> str:
        if not strs:
            return ""
        if len(strs) == 1:
            return strs[0]
        need_break = False
        prefix = ""
        for i in range(1, len(strs[0])+1):
            if need_break:
                break
            prefix = strs[0][:i]
            for j in strs:
                if prefix != j[:i]:
                    need_break = True
                    break
        if prefix and need_break:
            prefix = prefix[:-1]

        return prefix

if __name__ == '__main__':
    solution = Solution()
    grid = ["c","acc","ccc"]
    print(solution.longestCommonPrefix(grid))