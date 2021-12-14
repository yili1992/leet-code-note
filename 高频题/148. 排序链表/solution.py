#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: zhaoli01@corp.netease.com
@project: leet_code
@time: 2020-11-29 18:58
@desc:
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next




class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        def mergeTwoLists(l1, l2):
            """
            合并两个有序链表（21. 合并两个有序链表）
            :param l1:
            :param l2:
            :return:
            """
            sentry = ListNode(-1)
            curr = sentry
            while(l1 and l2):
                if l1.val<l2.val:
                    curr.next = l1
                    l1 = l1.next
                else:
                    curr.next = l2
                    l2 = l2.next
                curr = curr.next
            curr.next = l1 if l1 else l2
            return sentry.next


        def middle_node(m_head):
            """
            找到链表中间节点
            :param m_head:
            :return:
            """
            if not m_head or not m_head.next:
                return m_head
            slow = m_head
            fast = m_head.next.next
            while(fast and fast.next):
                slow = slow.next
                fast = fast.next.next

            return slow
        # 找到链表中间节点并断开链表 & 递归下探
        mid_node = middle_node(head)
        right_head = mid_node.next
        mid_node.next = None
        left = self.sortList(head)
        right = self.sortList(right_head)
        return mergeTwoLists(left, right)




if __name__ == '__main__':
    solution = Solution()
    head = ListNode(3, ListNode(5, ListNode(-1, ListNode(4, ListNode(0)))))
    result = solution.sortList(head)
    print(result)
