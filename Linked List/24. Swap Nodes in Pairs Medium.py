'''
Given a linked list, swap every two adjacent nodes and return its head.

You may not modify the values in the list's nodes, only nodes itself may be changed.



Example:

Given 1->2->3->4, you should return the list as 2->1->4->3.
'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(-1)
        dummy.next = head
        p = dummy
        n = dummy
        if p.next == None or p.next.next == None:
            return dummy.next
        p = p.next.next
        while p.next and p.next.next:
            m = n.next
            n.next = p
            m.next = p.next
            p.next = m
            p = m
            p = p.next.next
            n = n.next.next
        m = n.next
        n.next = p
        m.next = p.next
        p.next = m
        return dummy.next
