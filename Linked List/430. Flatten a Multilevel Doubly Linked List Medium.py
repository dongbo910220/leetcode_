'''
https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/
You are given a doubly linked list which in addition to the next and previous pointers, it could have a child pointer, which may or may not point to a separate doubly linked list. These child lists may have one or more children of their own, and so on, to produce a multilevel data structure, as shown in the example below.

Flatten the list so that all the nodes appear in a single-level, doubly linked list. You are given the head of the first level of the list.
'''


#理解错了题意，写了一个更难的版本
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""


class Solution(object):
    def flatten(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if head == None:
            return head
        p = head
        # while p:
        #     if p.child:
        #         p_child = self.findChild(p.child)
        #         p_tail = self.findTail(p)
        #         p_tail.next = p_child
        #     p = p.next
        p1, t1 = self.findChild(p)

        return head

    def findTail(self, head):
        p = head
        while p.next:
            p = p.next
        return p

    def findChild(self, head):
        p = head
        p_tail = self.findTail(p)
        while p:
            if p.child:
                p_child, p_newtail = self.findChild(p.child)
                # p_tail = self.findTail(p)
                p_tail.next = p_child
                p_child.prev = p_tail
                p_tail = p_newtail
                p.child = None
            if p.next == None:
                tail = p
            p = p.next
        return head, tail

'''
Success
Details 
Runtime: 28 ms, faster than 72.22% of Python online submissions for Flatten a Multilevel Doubly Linked List.
Memory Usage: 13.5 MB, less than 100.00% of Python online submissions for Flatten a Multilevel Doubly Linked List.
'''
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""


class Solution(object):
    def flatten(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if head == None:
            return head
        p = head
        # while p:
        #     if p.child:
        #         p_child = self.findChild(p.child)
        #         p_tail = self.findTail(p)
        #         p_tail.next = p_child
        #     p = p.next
        p1, t1 = self.findChild(p)

        return head

    def findTail(self, head):
        p = head
        while p.next:
            p = p.next
        return p

    def findChild(self, head):
        p = head
        while p:
            p_next = p.next
            if p_next == None:
                tail = p
            if p.child:
                p_child, p_childtail = self.findChild(p.child)
                # p_tail = self.findTail(p)

                p.next = p_child
                p_child.prev = p

                p_childtail.next = p_next
                if p_next:
                    p_next.prev = p_childtail
                else:  # p_next == None
                    tail = p_childtail
                p.child = None
            p = p_next
        return head, tail




