'''
Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

Example:

Input: head = 1->4->3->2->5->2, x = 3
Output: 1->2->2->4->3->5
'''

'''
Success
Details 
Runtime: 16 ms, faster than 96.42% of Python online submissions for Partition List.
Memory Usage: 11.9 MB, less than 25.00% of Python online submissions for Partition List.
'''


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
        dummy2 = ListNode(-2)
        dummy1.next = None
        p1 = dummy1
        dummy2.next = None
        p2 = dummy2
        p = head
        if p == None:
            return head
        while p:
            if p.val < x:
                p1.next = p
                p1 = p1.next
            else:
                p2.next = p
                p2 = p2.next
            p = p.next
        p1.next = None
        p2.next = None
        p1.next = dummy2.next
        return dummy1.next
