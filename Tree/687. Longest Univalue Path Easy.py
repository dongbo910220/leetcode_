'''
https://leetcode.com/problems/longest-univalue-path/

Success
Details
Runtime: 452 ms, faster than 53.10% of Python online submissions for Longest Univalue Path.
Memory Usage: 19.7 MB, less than 78.24% of Python online submissions for Longest Univalue Path.
'''



# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.maxLen = 0

        def dfs(node):
            if not node:
                return 0

            curLen = 0
            left = 0
            right = 0
            leftLen = dfs(node.left)
            rightLen = dfs(node.right)
            if node.left and node.left.val == node.val:
                left = leftLen + 1
            if node.right and node.right.val == node.val:
                right = rightLen + 1
            curLen = left + right

            self.maxLen = max(self.maxLen, curLen)
            return max(left, right)

        dfs(root)
        return self.maxLen