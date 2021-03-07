#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: zhaoli01@corp.netease.com
@project: leet_code
@time: 2020-11-29 18:58
@desc:
"""


class Solution(object):
    def verifyPostorder(self, postorder):
        """
        :type postorder: List[int]
        :rtype: bool
        """
        if not postorder:
            return True

        def isTree(postorder):
            root = postorder[-1]
            length = len(postorder)
            for i in range(length):  # 找到左子树的区间,此时注意下这样的切分不可能出现左子树中的节点比根节点大
                if postorder[i] > root:
                    break

            for j in range(i, length - 1):  # 如果右子树中存在比根节点的小的值,那么是不符合条件的
                if postorder[j] < root:
                    return False

            left = True
            if i > 0:
                left = isTree(postorder[:i])  # 判断左子树是否符合条件
            right = True
            if i < length - 1:
                right = isTree(postorder[i:-1])  # 判断右子树是否符合条件
            return left and right

        return isTree(postorder)


if __name__ == '__main__':
    solution = Solution()
    grid = [1,3,2,6,5]
    print(solution.verifyPostorder(grid))