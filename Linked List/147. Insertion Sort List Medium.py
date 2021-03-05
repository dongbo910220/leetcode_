'''

https://leetcode.com/problems/insertion-sort-list/
'''
'''
Success
Details 
Runtime: 2224 ms, faster than 6.79% of Python online submissions for Insertion Sort List.
Memory Usage: 16.2 MB, less than 14.29% of Python online submissions for Insertion Sort List.
'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head
        pre = head
        p = head.next
        dummy = ListNode(-100)
        dummy.next = head
        while p:
            p_next = p.next
            h = dummy.next
            while h.val < p.val and h.next.val < p.val:
                h = h.next
            if dummy.next.val > p.val:
                p.next = dummy.next
                dummy.next = p
                pre.next = p_next  # pre stop
                p = p_next
            elif h.next != p:
                pre.next = p.next
                p.next = h.next
                h.next = p
                p = p_next
            elif h.next == p:
                pre = p
                p = p_next
        return dummy.next

#easy to understand
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head
        dummy = ListNode(-100)
        pre = dummy
        cur = head
        next = None
        while cur:
            next = cur.next
            pre = dummy
            while pre.next and pre.next.val < cur.val:
                pre = pre.next
            cur.next = pre.next
            pre.next = cur
            cur = next
        return dummy.next
