# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(-1)
        dummy.next = head
        p1 = dummy
        for i in range(n):
            p1 = p1.next
        p2 = dummy
        while p1.next:
            p1 = p1.next
            p2 = p2.next
        #p2.next is to be deleted
        p2.next = p2.next.next
        return dummy.next