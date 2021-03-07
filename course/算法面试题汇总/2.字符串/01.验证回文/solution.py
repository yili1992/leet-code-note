#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: zhaoli01@corp.netease.com
@project: leet_code
@time: 2020-11-29 18:58
@desc:
"""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        tail = len(s) - 1
        for index, i in enumerate(s):
            if index == tail:
                break
            if not i.isalnum():
                continue
            else:
                while True:
                    if not s[tail].isalnum():
                        tail -=1
                    else:
                        break
                if i != s[tail]:
                    return False
                else:
                    tail -= 1
        return True


if __name__ == '__main__':
    solution = Solution()
    print(solution.isPalindrome("A man, a plan, a canal: Panama"))