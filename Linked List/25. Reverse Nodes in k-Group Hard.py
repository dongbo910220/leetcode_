'''
Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

Example:

Given this linked list: 1->2->3->4->5

For k = 2, you should return: 2->1->4->3->5

For k = 3, you should return: 3->2->1->4->5

Note:

Only constant extra memory is allowed.
You may not alter the values in the list's nodes, only nodes itself may be changed.
'''

'''
Success
Details 
Runtime: 40 ms, faster than 66.47% of Python online submissions for Reverse Nodes in k-Group.
Memory Usage: 14.5 MB, less than 5.26% of Python online submissions for Reverse Nodes in k-Group.

'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        dummy = ListNode(-1)
        dummy.next = head
        tail = dummy
        start = dummy
        p = dummy
        if k == 1:
            return dummy.next
        while p:
            for i in range(k):
                if p:
                    p = p.next
            if p:
                # next start
                p_next = p.next
                # reverse it the k-link and get the reversed start and tail
                rev_start, rev_tail = self.reverse(start.next, p)
                #old start
                start.next = rev_start
                rev_tail.next = p_next
                p = rev_tail
                #new start
                start = p
            else:
                break
        return dummy.next

    def reverse(self, head, tail):
        p1 = head
        p2 = head.next
        while p2 != tail:
            p3 = p2.next
            p2.next = p1
            p1 = p2
            p2 = p3
        # p2 is tail
        p2.next = p1
        return p2, head


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head == None or head.next == None or k == 1:
            return head
        dummy = ListNode(-1)
        dummy.next = head
        tail = dummy
        p = dummy
        while p:
            for i in range(k):
                if p:
                    p = p.next
            if p:
                p_next = p.next
                tail.next, p = self.reverse(tail.next, p)
                p.next = p_next
                tail = p
            else:
                break
        return dummy.next

    def reverse(self, head, tail):
        p1 = head
        p2 = head.next
        while p2 != tail:
            p3 = p2.next
            p2.next = p1
            p1 = p2
            p2 = p3
        p2.next = p1
        return p2, head

a = [2, 2]
print(a[0:2])