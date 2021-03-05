# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        dummy1 = ListNode(-1)
        less = dummy1
        dummy2 = ListNode(-1)
        large = dummy2
        p = head
        while p:
            if p.val < x:
                less.next = p
                less = p
            else:
                large.next = p
                large = p
            p = p.next
        large.next = None
        less.next = dummy2.next
        return dummy1.next