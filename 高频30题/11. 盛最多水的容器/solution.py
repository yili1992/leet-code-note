#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: zhaoli01@corp.netease.com
@project: leet_code
@time: 2020-11-29 18:58
@desc:
"""

class Solution:
    def maxArea(self, height: list) -> int:
        if not height:
            return 0
        else:
            max_area = 0
            head = 0
            tail = len(height)-1
            while head != tail:
                if height[head] <= height[tail]:
                    current_hight = height[head]
                    current_area = current_hight * (tail - head)
                    head += 1
                else:
                    current_hight = height[tail]
                    current_area = current_hight * (tail - head)
                    tail -= 1
                max_area = max(max_area, current_area)
            return max_area




if __name__ == '__main__':
    solution = Solution()
    grid = [4,3,2,1,4]
    print(solution.maxArea(grid))