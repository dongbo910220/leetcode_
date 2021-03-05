'''
Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
Follow up:

A linked list can be reversed either iteratively or recursively. Could you implement both?
'''

'''
Success
Details 
Runtime: 20 ms, faster than 87.94% of Python online submissions for Reverse Linked List.
Memory Usage: 13.7 MB, less than 28.70% of Python online submissions for Reverse Linked List.
'''


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head

        dummy = ListNode(-1)
        dummy.next = head
        p1 = head
        p2 = head.next
        p3 = head.next.next
        while p3:
            p2.next = p1
            p1 = p2
            p2 = p3
            p3 = p3.next
        p2.next = p1
        start = p2
        dummy.next.next = None
        return start

