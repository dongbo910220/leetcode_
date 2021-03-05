'''
https://leetcode.com/problems/minimum-depth-of-binary-tree/
'''
'''
Success
Details 
Runtime: 24 ms, faster than 97.31% of Python online submissions for Minimum Depth of Binary Tree.
Memory Usage: 15.6 MB, less than 5.13% of Python online submissions for Minimum Depth of Binary Tree.
'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.height = 0

    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.depth(root)

    def depth(self, root):
        if not root:
            return 0
        if root and not root.left and not root.right:
            return 1
        leftHeight = self.depth(root.left)
        if leftHeight == 0:
            leftHeight = float('inf')
        rightHeight = self.depth(root.right)
        if rightHeight == 0:
            rightHeight = float('inf')
        return min(leftHeight, rightHeight) + 1

