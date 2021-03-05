'''
You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Follow up:
What if you cannot modify the input lists? In other words, reversing the lists is not allowed.

Example:

Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 8 -> 0 -> 7
'''
'''
Success
Details 
Runtime: 44 ms, faster than 100.00% of Python online submissions for Add Two Numbers II.
Memory Usage: 13 MB, less than 6.67% of Python online submissions for Add Two Numbers II.

'''


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

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
        p1 = l1
        p2 = l2
        num1 = 0
        num2 = 0
        while p1:
            num1 *= 10
            num1 += p1.val
            p1 = p1.next
        while p2:
            num2 *= 10
            num2 += p2.val
            p2 = p2.next
        total = num1 + num2
        dummy = ListNode(-1)
        if total == 0:
            return ListNode(0)

        while total:
            num = total % 10
            p = ListNode(num)
            p.next = dummy.next
            dummy.next = p
            total = total // 10
        return dummy.next