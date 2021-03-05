'''
https://leetcode.com/problems/invert-binary-tree/
'''

'''
Success
Details 
Runtime: 20 ms, faster than 49.15% of Python online submissions for Invert Binary Tree.
Memory Usage: 12.8 MB, less than 5.00% of Python online submissions for Invert Binary Tree.

'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root

