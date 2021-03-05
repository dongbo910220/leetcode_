'''
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4

'''


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
'''
Success
Details
Runtime: 20 ms, faster than 91.42% of Python online submissions for Merge Two Sorted Lists.
Memory Usage: 11.8 MB, less than 55.17% of Python online submissions for Merge Two Sorted Lists.

'''
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        start1 = l1
        start2 = l2
        output = ListNode(-1)
        start = output
        while start1 != None and start2 != None:
            if start1.val < start2.val:
                output.next = start1
                output = output.next
                start1 = start1.next
            else:
                output.next = start2
                output = output.next
                start2 = start2.next
        if start1 != None:
            output.next = start1
        else:
            output.next = start2
        start = start.next
        return start


