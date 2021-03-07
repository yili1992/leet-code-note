#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: zhaoli01@corp.netease.com
@project: leet_code
@time: 2021-01-10 18:58
@desc:
"""


class Solution:
    def wordBreak(self, s: str, wordDict: list) -> list:
        def recall(s:str, subres:list, result:list):
            if not s:
                result.append(' '.join(subres))
            for word in wordDict:
                if s.startswith(word):
                    subres.append(word)
                    recall(s[len(word):], subres, result)
                    subres.pop()

        def is_check(s) ->bool:
            dp = [False for i in range(len(s) + 1)]
            dp[0] = True

            for i in range(len(s)):
                if dp[i] == True:
                    for j in range(i + 1, len(s) + 1):
                        if s[i:j] in wordDict:
                            dp[j] = True

            return dp[-1]
        if not is_check(s):
            return []
        subres = []
        result = []
        recall(s, subres, result)
        return result

if __name__ == '__main__':
    solution = Solution()
    s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    wordDict = ["a", "aa", "aaa", "aaaa", "aaaaa", "aaaaaa", "aaaaaaa", "aaaaaaaa", "aaaaaaaaa", "aaaaaaaaaa"]
    print(solution.wordBreak(s, wordDict))