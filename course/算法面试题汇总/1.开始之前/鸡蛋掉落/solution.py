#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: zhaoli01@corp.netease.com
@project: leet_code
@time: 2020-11-22 13:52
@desc:
"""
class Solution:
    def superEggDrop(self, K: int, N: int) -> int:
        dp = [[0 for _ in range(N + 1)] for _ in range(K + 1)]
        for i in range(1, K + 1):
            for step in range(1, N + 1):
                dp[i][step] = dp[i - 1][step - 1] + (dp[i][step - 1] + 1)
                if dp[K][step] >= N:
                    return step
        return 0


if __name__ == '__main__':
    solution = Solution()
    print(solution.superEggDrop(2,6))