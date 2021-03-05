'''
https://leetcode.com/problems/univalued-binary-tree/submissions/

Success
Details
Runtime: 24 ms, faster than 32.08% of Python online submissions for Univalued Binary Tree.
Memory Usage: 13 MB, less than 7.90% of Python online submissions for Univalued Binary Tree.
'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        value = root.val

        def dfs(s):
            if not s:
                return True

            if s.val != value:
                return False

            return dfs(s.left) and dfs(s.right)

        return dfs(root)