'''
https://leetcode.com/problems/copy-list-with-random-pointer/
'''
'''
A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.

Return a deep copy of the list.

The Linked List is represented in the input/output as a list of n nodes. Each node is represented as a pair of [val, random_index] where:

val: an integer representing Node.val
random_index: the index of the node (range from 0 to n-1) where random pointer points to, or null if it does not point to any node.

'''
"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if head is None:
            return None
        dict = {}
        cur = head
        id = 0
        while cur:
            dict[cur] = Node(cur.val, None, None)
            cur = cur.next

        cur = head
        while cur:
            if cur.next:
                dict[cur].next = dict[cur.next]
            if cur.random:
                dict[cur].random = dict[cur.random]
            cur =cur.next

        return dict[head]



