BFS广度优先遍历
```buildoutcfg
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        #跟结点入queue
        queue = [root]
        res = []
        while queue:
            res.append([node.val for node in queue])
            #存储当前层的孩子节点列表
            ll = []
            #对当前层的每个节点遍历
            for node in queue:
                #如果左子节点存在，入队列
                if node.left:
                    ll.append(node.left)
                #如果右子节点存在，入队列
                if node.right:
                    ll.append(node.right)
            #后把queue更新成下一层的结点，继续遍历下一层
            queue = ll
        return res
```