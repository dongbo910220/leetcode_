'''
https://leetcode.com/problems/n-ary-tree-preorder-traversal/submissions/

Success
Details
Runtime: 40 ms, faster than 90.83% of Python online submissions for N-ary Tree Preorder Traversal.
Memory Usage: 15.8 MB, less than 88.66% of Python online submissions for N-ary Tree Preorder Traversal
'''

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if not root:
            return []
        res = []
        self.dfs(root, res)
        return res

    def dfs(self, root, res):
        if root:
            res.append(root.val)
            for node in root.children:
                self.dfs(node, res)
        else:
            return


"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if not root:
            return []
        res = []
        stack = [root]
        while stack:
            cur = stack.pop()
            res.append(cur.val)
            stack.extend(reversed(cur.children))
        return res