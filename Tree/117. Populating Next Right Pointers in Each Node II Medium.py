'''
Given a binary tree

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.
https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/

'''
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
'''
Success
Details 
Runtime: 68 ms, faster than 7.65% of Python online submissions for Populating Next Right Pointers in Each Node II.
Memory Usage: 15.5 MB, less than 100.00% of Python online submissions for Populating Next Right Pointers in Each Node II.
'''

class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return None
        current = [root]

        while current:
            next_level = []
            prev_node = None
            for node in current:
                if node.right:
                    next_level.append(node.right)
                if node.left:
                    next_level.append(node.left)
                node.next = prev_node
                prev_node = node
            current = next_level

        return root

# # print(abs(-1))
# a = 1
# b = 1
# def add(a, b):
#     c = a + b
#     a = a+ 1
#     print("a", a)
#     return c
#
# print("a_original", a)
# print(add(a, b))
# print("a_original", a)



