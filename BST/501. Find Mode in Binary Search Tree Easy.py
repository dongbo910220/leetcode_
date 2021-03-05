'''
https://leetcode.com/problems/find-mode-in-binary-search-tree/submissions/

Success
Details
Runtime: 60 ms, faster than 33.98% of Python online submissions for Find Mode in Binary Search Tree.
Memory Usage: 20.5 MB, less than 77.92% of Python online submissions for Find Mode in Binary Search Tree.
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        h = collections.Counter()
        if not root:
            return []

        def dfs(node):
            if not node:
                return
            h[node.val] += 1
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        maxCount = max(h.values())
        return [i for i in h if h[i] == maxCount]