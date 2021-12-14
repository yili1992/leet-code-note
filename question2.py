#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: zhaoli01@corp.netease.com
@project: leet_code
@time: 2021/8/19 10:25 下午
@desc:
"""
import bisect
sort_list = []
sort_list2 = []


def add_element(i: int):
    """
    bisect是python 二分查找操作的库，自己写项目会直接用这个
    :return:
    """
    bisect.insort(sort_list, i)


def add_element2(i: int):
    n = len(sort_list2)
    if n == 0:
        sort_list2.append(i)
        return
    if i >= sort_list2[-1]:
        sort_list2.append(i)
        return
    if i <= sort_list2[0]:
        sort_list2.insert(0, i)
        return
    left, right = 0, n - 1
    ans = -1
    while left <= right:
        mid = (left + right) // 2
        if i <= sort_list2[mid]:
            right = mid - 1
            ans = mid
        else:
            left = mid + 1
    sort_list2.insert(ans, i)
    return


if __name__ == '__main__':
    add_element(50)
    add_element(10)
    add_element(999)
    add_element(3)
    add_element(3)
    add_element(-1)
    print(sort_list)
    add_element2(50)
    add_element2(10)
    add_element2(999)
    add_element2(3)
    add_element2(3)
    add_element2(-1)
    print(sort_list2)
