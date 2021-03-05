'''
Given a sorted linked list, delete all duplicates such that each element appear only once.

Example 1:

Input: 1->1->2
Output: 1->2

Example 2:

Input: 1->1->2->3->3
Output: 1->2->3

'''
'''
Success
Details
Runtime: 28 ms, faster than 80.16% of Python online submissions for Remove Duplicates from Sorted List.
Memory Usage: 11.8 MB, less than 64.29% of Python online submissions for Remove Duplicates from Sorted List.

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
        tag = False
        start = head
        while head != None:
            if tag == False:
                lastval = head.val
                pre = head
                head = head.next
                tag = True
            else:
                if head.val == lastval:
                    pre.next = head.next
                    head = head.next
                else:
                    lastval = head.val
                    pre = head
                    head = head.next
        return start



