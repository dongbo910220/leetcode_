'''You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
'''
'''
Success
Details 
Runtime: 64 ms, faster than 48.87% of Python online submissions for Add Two Numbers.
Memory Usage: 11.9 MB, less than 28.68% of Python online submissions for Add Two Numbers.
'''


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        num1 = 0
        head1 = l1
        i = 1
        while head1:
            num1 += head1.val * i
            i = i * 10
            head1 = head1.next

        num2 = 0
        head2 = l2
        i = 1
        while head2:
            num2 += head2.val * i
            i = i * 10
            head2 = head2.next

        num_total = num1 + num2
        if num_total == 0:
            return ListNode(0)

        dummy = ListNode(-1)
        head = dummy
        while num_total:
            num = num_total % 10
            tmp = ListNode(num)
            head.next = tmp
            head = head.next
            num_total = num_total // 10
        return dummy.next
