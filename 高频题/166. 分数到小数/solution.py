#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: zhaoli01@corp.netease.com
@project: leet_code
@time: 2020-11-29 18:58
@desc:
"""
from functools import reduce

class Solution:
    def fractionToDecimal(self, numerator, denominator):
        if numerator == 0:
            return "0"
        res = []
        if (numerator < 0) ^ (denominator < 0):  # 正负号判断，异或
            res.append("-")

        numer = abs(numerator)  # 取整
        denomin = abs(denominator)

        a, remaind = divmod(numer, denomin)
        res.append(str(a))
        if remaind == 0:  # 整除，直接返回
            return "".join(res)

        res.append(".")  # 添加小数点
        dic = {}
        while remaind != 0:
            if remaind in dic:  # 如果有循环，添加括号
                res.insert(dic[remaind], "(")
                print(dic[remaind])
                res.append(")")
                break

            dic[remaind] = len(res)  # 记录括号的位置
            remaind *= 10  # 余数加0，继续除法
            a, remaind = divmod(remaind, denomin)
            res.append(str(a))

        return "".join(res)


if __name__ == '__main__':
    solution = Solution()
    numerator = 1
    denominator = 6
    result = solution.fractionToDecimal(numerator, denominator)
    print(result)
