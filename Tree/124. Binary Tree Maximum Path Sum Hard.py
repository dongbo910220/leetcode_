'''
https://leetcode.com/problems/binary-tree-maximum-path-sum/submissions/
'''
'''
Success
Details 
Runtime: 76 ms, faster than 90.22% of Python online submissions for Binary Tree Maximum Path Sum.
Memory Usage: 25.1 MB, less than 42.50% of Python online submissions for Binary Tree Maximum Path Sum.
'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.maximum = -float('inf')

    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        self.findMaximumPath(root)
        return self.maximum

    def findMaximumPath(self, root):
        if not root:
            return 0
        leftMaximum = self.findMaximumPath(root.left)
        rightMaximum = self.findMaximumPath(root.right)
        currentMaximum = max(root.val, root.val + leftMaximum, root.val + rightMaximum,
                             root.val + leftMaximum + rightMaximum)
        singlePath = max(root.val, root.val + leftMaximum, root.val + rightMaximum)
        if currentMaximum > self.maximum:
            self.maximum = currentMaximum
        return singlePath


# def aaa():
#     return 1
# b = aaa()
# print(b)
# print(b.__class__)
# print(b[0])
