'''
https://leetcode.com/problems/binary-tree-cameras/
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minCameraCover(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = 0
        def dfs(root):
            if not root:
                return 2
            l, r = dfs(root.left), dfs(root.right)
            if l == 2 and r == 2:
                return 0
            if l == 0 or r == 0:
                self.res += 1
                return 1
            if l == 1 or r == 1:
                return 2
        return int(dfs(root)==0) + self.res
'''
Success
Details
Runtime: 32 ms, faster than 70.40% of Python online submissions for Binary Tree Cameras.
Memory Usage: 13.3 MB, less than 33.33% of Python online submissions for Binary Tree Cameras.
'''