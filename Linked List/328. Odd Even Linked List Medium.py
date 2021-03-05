'''
Given a singly linked list, group all odd nodes together followed by the even nodes. Please note here we are talking about the node number and not the value in the nodes.

You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.

Example 1:

Input: 1->2->3->4->5->NULL
Output: 1->3->5->2->4->NULL
Example 2:

Input: 2->1->3->5->6->4->7->NULL
Output: 2->3->6->7->1->5->4->NULL
'''
'''
Success
Details 
Runtime: 36 ms, faster than 40.31% of Python online submissions for Odd Even Linked List.
Memory Usage: 15.5 MB, less than 15.00% of Python online submissions for Odd Even Linked List.
'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head
        dummy1 = ListNode(-1)
        dummy2 = ListNode(-2)
        tail1 = dummy1
        tail2 = dummy2
        p1 = head
        p2 = head.next
        while p1 and p2:  # think it more
            tail1.next = p1
            tail2.next = p2
            tail1 = tail1.next
            tail2 = tail2.next
            p1 = p2.next
            if p2.next:
                p2 = p2.next.next
            else:
                p2.next = None
        if p1:
            tail1.next = p1
            tail1 = tail1.next
            tail1.next = None
        else:
            tail1.next = None
        tail2.next = None
        tail1.next = dummy2.next
        return dummy1.next