'''
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

Example:

Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6


'''

#Time Limit Exceeded
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#Time Limit Exceeded
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        dummy = ListNode(-1)
        tail = dummy
        if lists == None:
            return None
        n = len(lists)
        start = [0] * n
        small = float("inf")
        the_idx = 0
        sum = 0
        for i in range(len(lists)):
            p = lists[i]
            # if p != None:
            #     sum += 1
            while (p != None):
                p = p.next
                sum += 1
                # print(sum)
        # sum  = 3
        while sum:
            # print(sum)
            for i in range(len(lists)):
                p = lists[i]
                if p != None:
                    if p.val <= small:
                        small = p.val
                        the_idx = i
            tail.next = lists[the_idx]
            tail = tail.next
            q = lists[the_idx]
            if q:
                q = q.next
                lists[the_idx] = q
            small = float("inf")
            sum -= 1
        tail.next = None
        return dummy.next

#学习了heap的相关使用
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if lists == None:
            return None
        dummy = ListNode(-1)
        tail = dummy
        h = [(node.val, node) for node in lists if node]
        heapify(h)
        while h:
            val, node = h[0]
            if node.next is None:
                heappop(h)
            else:
                heapreplace(h, (node.next.val, node.next))
            tail.next = node
            tail = tail.next
        return dummy.next
