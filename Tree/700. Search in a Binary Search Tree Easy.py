'''
https://leetcode.com/problems/search-in-a-binary-search-tree/

Success
Details
Runtime: 80 ms, faster than 27.04% of Python online submissions for Search in a Binary Search Tree.
Memory Usage: 16.8 MB, less than 37.52% of Python online submissions for Search in a Binary Search Tree.
'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """

        def dfs(root):
            if not root:
                return None
            if root.val == val:
                return root
            else:
                return dfs(root.left) or dfs(root.right)

        node = dfs(root)

        return node