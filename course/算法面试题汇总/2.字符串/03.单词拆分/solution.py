#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: zhaoli01@corp.netease.com
@project: leet_code
@time: 2021-01-10 18:58
@desc:
"""


class Solution:
    def wordBreak(self, s: str, wordDict: list) -> bool:
        dp = [False for i in range(len(s) + 1)]
        dp[0] = True

        for i in range(len(s)):
            if dp[i] == True:
                for j in range(i + 1, len(s) + 1):
                    if s[i:j] in wordDict:
                        dp[j] = True

        return dp[-1]


if __name__ == '__main__':
    solution = Solution()
    s = "catsandog"
    wordDict = ["cats", "dog", "sand", "and", "cat"]
    print(solution.wordBreak(s, wordDict))