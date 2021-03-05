'''
You are given a perfect binary tree where all leaves are on the same level, and every parent has two children. The binary tree has the following definition:

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.
https://leetcode.com/problems/populating-next-right-pointers-in-each-node/
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
Runtime: 88 ms, faster than 5.63% of Python online submissions for Populating Next Right Pointers in Each Node.
Memory Usage: 15.8 MB, less than 8.00% of Python online submissions for Populating Next Right Pointers in Each Node.
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