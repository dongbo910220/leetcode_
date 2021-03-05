'''
Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

Return the linked list sorted as well.

Example 1:

Input: 1->2->3->3->4->4->5
Output: 1->2->5
Example 2:

Input: 1->1->1->2->3
Output: 2->3
'''
'''
Success
Details 
Runtime: 28 ms, faster than 74.81% of Python online submissions for Remove Duplicates from Sorted List II.
Memory Usage: 11.7 MB, less than 93.75% of Python online submissions for Remove Duplicates from Sorted List II.

'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(-1)
        p = dummy
        cur = head
        dummy.next = head
        while cur:
            if cur.next and cur.next.val == cur.val:
                while cur.next and cur.next.val == cur.val:
                    cur = cur.next
                p.next = cur.next
            else:
                p = p.next
            cur = cur.next
        return dummy.next

