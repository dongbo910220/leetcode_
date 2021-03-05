'''
执行结果：
通过
显示详情
执行用时：76 ms, 在所有 Python 提交中击败了89.83% 的用户
内存消耗：30.4 MB, 在所有 Python 提交中击败了72.54% 的用户
'''


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        if not head:
            return
        vec = []
        node = head
        while node:
            vec.append(node)
            node = node.next

        i, j = 0, len(vec) - 1
        while i < j:
            vec[i].next = vec[j]
            i += 1
            if i == j:
                break
            vec[j].next = vec[i]
            j -= 1
        vec[i].next = None