#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: zhaoli01@corp.netease.com
@project: leet_code
@time: 2020-11-29 18:58
@desc:
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def levelOrder(self, root: TreeNode):

        result = []
        if not root: return result

        def bfs(node:TreeNode, deep: int):
            if len(result) <= deep:
                result.append([node.val])
            else:
                result[deep].append(node.val)
            if node.left:
                bfs(node.left, deep+1)
            if node.right:
                bfs(node.right, deep+1)
        bfs(root, 0)
        return result


if __name__ == '__main__':
    solution = Solution()
    grid = [3,9,20,None,None,15,7]
    treenodee =TreeNode(3, TreeNode(9), TreeNode(20))

    print(solution.levelOrder(treenodee))

    # [
    #     [3],
    #     [9, 20],
    #     [15, 7]
    # ]