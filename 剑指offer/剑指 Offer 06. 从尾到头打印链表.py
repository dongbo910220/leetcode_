'''
执行结果：
通过
显示详情
执行用时：116 ms, 在所有 Python 提交中击败了15.25% 的用户
内存消耗：22.9 MB, 在所有 Python 提交中击败了10.59% 的用户
'''


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reversePrint(self, head):
        """
        :type head: ListNode
        :rtype: List[int]
        """
        if head == None:
            return []
        else:
            return self.reversePrint(head.next) + [head.val]