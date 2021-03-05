'''
https://leetcode.com/problems/binary-tree-pruning/

Success
Details
Runtime: 12 ms, faster than 98.78% of Python online submissions for Binary Tree Pruning.
Memory Usage: 12.8 MB, less than 50.51% of Python online submissions for Binary Tree Pruning.
'''


# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pruneTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """

        def dfs(s):
            if not s:
                return True
            isLeft = dfs(s.left)
            if isLeft:
                s.left = None
            isRight = dfs(s.right)
            if isRight:
                s.right = None
            if s.val == 0 and isLeft and isRight:
                return True
            else:
                return False

        dfs(root)
        return root
