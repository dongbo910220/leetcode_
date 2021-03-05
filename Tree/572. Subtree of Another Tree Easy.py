'''
https://leetcode.com/problems/subtree-of-another-tree/


Success
Details
Runtime: 228 ms, faster than 81.59% of Python online submissions for Subtree of Another Tree.
Memory Usage: 14.2 MB, less than 18.44% of Python online submissions for Subtree of Another Tree.

'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """

        def check(s, t):
            if not s and not t:
                return True

            if not s and t:
                return False

            if not t and s:
                return False

            if t.val != s.val:
                return False

            return check(s.left, t.left) and check(s.right, t.right)

        def dfs(s, t):
            if not s:
                return False

            if s.val == t.val and check(s, t):
                return True

            return dfs(s.left, t) or dfs(s.right, t)

        return dfs(s, t)