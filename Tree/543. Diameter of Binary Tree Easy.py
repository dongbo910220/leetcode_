'''
https://leetcode.com/problems/diameter-of-binary-tree/

Success
Details
Runtime: 20 ms, faster than 99.87% of Python online submissions for Diameter of Binary Tree.
Memory Usage: 15.6 MB, less than 71.80% of Python online submissions for Diameter of Binary Tree.
'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        # longestPath = 0

        def dfs(node):
            if not node:
                return 0
            leftPath = dfs(node.left)
            rightPath = dfs(node.right)
            currentPath = leftPath + rightPath
            if currentPath > self.longestPath:
                self.longestPath = currentPath
            return max(leftPath, rightPath) + 1

        self.longestPath = 0
        dfs(root)
        return self.longestPath