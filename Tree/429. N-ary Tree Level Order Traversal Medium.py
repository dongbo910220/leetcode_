'''
https://leetcode.com/problems/n-ary-tree-level-order-traversal/


Success
Details
Runtime: 36 ms, faster than 95.70% of Python online submissions for N-ary Tree Level Order Traversal.
Memory Usage: 15.8 MB, less than 62.26% of Python online submissions for N-ary Tree Level Order Traversal.
'''


"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        if not root:
            return []
        res = []
        queue = [root]
        while queue:
            cur = []
            new_queue = []
            for node in queue:
                cur.append(node.val)
                for node_son in node.children:
                    new_queue.append(node_son)
            res.append(cur)
            queue = new_queue
        return res