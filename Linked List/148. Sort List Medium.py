'''
Sort a linked list in O(n log n) time using constant space complexity.

Example 1:

Input: 4->2->1->3
Output: 1->2->3->4
Example 2:

Input: -1->5->3->4->0
Output: -1->0->3->4->5

Success
Details
Runtime: 232 ms, faster than 77.41% of Python online submissions for Sort List.
Memory Usage: 29.7 MB, less than 38.46% of Python online submissions for Sort List.

'''


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        mid = slow.next
        slow.next = None
        l1 = self.sortList(head)
        l2 = self.sortList(mid)
        return self.merge(l1, l2)

    def merge(self, l1, l2):
        dummy = ListNode(-1)
        tail = dummy
        while l1 and l2:
            if l1.val > l2.val:
                l1, l2 = l2, l1
            tail.next = l1
            tail = tail.next
            l1 = l1.next
        if l1:
            tail.next = l1
        if l2:
            tail.next = l2
        return dummy.next

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        slow = head
        fast = slow.next
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        mid = slow.next
        # 断开
        slow.next = None
        l1 = self.sortList(head)
        l2 = self.sortList(mid)
        return self.merge(l1, l2)

    def merge(self, l1, l2):
        dummy = ListNode(-1)
        tail = dummy
        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                tail = tail.next
                l1 = l1.next
            else:
                tail.next = l2
                tail = tail.next
                l2 = l2.next
        if l1:
            tail.next = l1
        if l2:
            tail.next = l2
        return dummy.next

# Definition for singly-linked list. O(n) 复杂度方法
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        dummy = ListNode(-1); dummy.next = head; tmp = head
        length = 0
        while tmp:
            tmp = tmp.next
            length += 1
        step = 1
        while step < length:
            cur, new_head = dummy.next, dummy
            while cur:
                left = cur
                right = self.split(left, step)
                cur = self.split(right, step)
                new_head = self.merge(left, right, new_head)
            step <<= 1
        return dummy.next

    # divide the linked list into two lists
    # first linked list contains n nodes
    # return the head of second linked list
    def split(self, head, n):
        for i in range(n-1):
            if head:
                head = head.next
            else:
                break
        if not head:
            return None
        second = head.next
        # cut the link
        head.next = None
        return second

    # merge 2 sorted lists, and append the result to head
    # return the tail
    def merge(self, p1, p2, new_head):
        p = new_head
        while p1 and p2:
            if p1.val > p2.val:
                p1, p2 = p2, p1
            #p1 is the small one
            p.next = p1
            p = p.next
            p1 = p1.next
        if p1:
            p.next = p1
        if p2:
            p.next = p2
        while p.next:
            p = p.next
        return p