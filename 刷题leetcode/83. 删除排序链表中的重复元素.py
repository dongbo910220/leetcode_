# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        p = head.next
        cur = head
        while p :
            if p.val == cur.val:
                cur.next = p.next
                p = p.next
            else:
                cur = p
                p = p.next
        return head