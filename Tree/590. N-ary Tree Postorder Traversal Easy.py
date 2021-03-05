'''
https://leetcode.com/problems/n-ary-tree-postorder-traversal/submissions/

Success
Details
Runtime: 60 ms, faster than 20.76% of Python online submissions for N-ary Tree Postorder Traversal.
Memory Usage: 15.9 MB, less than 29.07% of Python online submissions for N-ary Tree Postorder Traversal.
'''


"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if not root:
            return []
        stack = [root]
        res = []
        while stack:
            node = stack[-1]
            if not node.children:
                res.append(node.val)
                stack.pop()
            else:
                stack.extend(reversed(node.children))
                node.children = []
        return res