'''
Given a linked list, remove the n-th node from the end of list and return its head.

Example:

Given linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:

Given n will always be valid.

Follow up:

Could you do this in one pass?
'''
'''
Success
Details 
Runtime: 24 ms, faster than 37.68% of Python online submissions for Remove Nth Node From End of List.
Memory Usage: 11.9 MB, less than 8.16% of Python online submissions for Remove Nth Node From End of List.
'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(-1)
        dummy.next = head
        p = dummy
        node = dummy
        for i in range(n):
            p = p.next
        while p.next:
            node = node.next
            p = p.next
        node.next = node.next.next
        return dummy.next

