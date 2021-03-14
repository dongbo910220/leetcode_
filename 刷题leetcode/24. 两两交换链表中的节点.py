'''
执行结果：
通过
显示详情
执行用时：16 ms, 在所有 Python 提交中击败了89.80% 的用户
内存消耗：12.9 MB, 在所有 Python 提交中击败了90.30% 的用户
'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        dummy = ListNode(-1)
        dummy.next = head

        start = dummy
        p1 = start.next
        # print(p1)
        while p1 and p1.next:
            p2 = p1.next
            p3 = p2.next
            p2.next = p1
            start.next = p2
            p1.next = p3
            start = start.next.next  #p1
            p1 = p3
        return dummy.next