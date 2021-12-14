#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: zhaoli01@corp.netease.com
@project: leet_code
@time: 2020-11-29 18:58
@desc:
"""


class MyCalendar:

    def __init__(self):
        self.cal = {}
        self.head = None

    def book(self, start: int, end: int) -> bool:
        if not self.cal:
            self.cal[(start, end)] = -1
            self.head = (start, end)
            return True
        node = self.head
        while node != -1:
            if node[1] <= start and (self.cal[node] == -1 or self.cal[node][0] >= end):
                self.cal[(start, end)] = self.cal[node]
                self.cal[node] = (start, end)
                return True
            node = self.cal[node]
        return False


# Your MyCalendar object will be instantiated and called as such:
obj = MyCalendar()
print(obj.book(47, 50))
print(obj.book(33, 41))
print(obj.book(39, 45))
print(obj.book(33, 42))
print(obj.book(25, 32))
print(obj.book(26, 35))
print(obj.cal)
print(obj.book(19, 25))


if __name__ == '__main__':
    solution = MyCalendar()
    left = 1
    right = 22