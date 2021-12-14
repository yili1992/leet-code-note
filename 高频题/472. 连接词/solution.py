#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: zhaoli01@corp.netease.com
@project: leet_code
@time: 2020-11-29 18:58
@desc:
"""

class preTreeNode(object):

    def __init__(self, value, next=None):
        super().__init__()
        self.value = value
        self.next = next


class Solution:
    def findAllConcatenatedWordsInADict(self, words:list) -> list:
        words = sorted(words, key=lambda i: len(i))
        s = set(words)
        ans = []
        while words:
            word = words.pop(-1)
            s.remove(word)
            L = len(word)
            stack = [0]
            while stack:
                p = stack.pop(0)
                flag = False
                for i in range(p + 1, L + 1):
                    if word[p:i] in s:
                        stack.append(i)
                        if i == L:
                            ans.append(word)
                            flag = True
                            break
                if flag: break
        return ans


if __name__ == '__main__':
    solution = Solution()
    words = ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]
    words2 = ["a","b","ab","abc"]
    result = solution.findAllConcatenatedWordsInADict(words)
    print(result)
