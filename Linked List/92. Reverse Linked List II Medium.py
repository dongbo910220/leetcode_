'''
Reverse a linked list from position m to n. Do it in one-pass.

Note: 1 ≤ m ≤ n ≤ length of list.

Example:

Input: 1->2->3->4->5->NULL, m = 2, n = 4
Output: 1->4->3->2->5->NULL

'''
'''
Success
Details 
Runtime: 16 ms, faster than 81.81% of Python online submissions for Reverse Linked List II.
Memory Usage: 11.8 MB, less than 100.00% of Python online submissions for Reverse Linked List II.
'''


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(-1)
        dummy.next = head
        pm = dummy
        # pre = dummy
        for i in range(m - 1):
            pm = pm.next
        pre = pm
        pm = pm.next
        end = dummy
        for i in range(n):
            end = end.next
        end = end.next

        k = n - m
        if k == 0:
            return head
        # k == 1?
        p1 = pm
        p2 = pm.next
        p3 = pm.next.next
        p1.next = end  # tail connection
        for i in range(k):
            if p3:
                p2.next = p1
                p1 = p2
                p2 = p3
                p3 = p3.next
            else:
                p2.next = p1
                p1 = p2
                p2 = p3

        pre.next = p1
        return dummy.next

