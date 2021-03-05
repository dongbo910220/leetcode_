'''
https://leetcode.com/problems/leaf-similar-trees/


通过
'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """

        def dfs(s, res):
            if s.left:
                dfs(s.left, res)
            if s.right:
                dfs(s.right, res)
            if not s.left and not s.right:
                res.append(s.val)

        res1 = []
        res2 = []
        dfs(root1, res1)
        dfs(root2, res2)
        return res1 == res2