'''
https://leetcode.com/problems/distribute-coins-in-binary-tree/
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.total = 0

    def distributeCoins(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def dfs(root):
            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            need = root.val + left + right - 1
            self.total += abs(need)
            return need

        dfs(root)
        return self.total


'''

Success
Details 
Runtime: 20 ms, faster than 96.22% of Python online submissions for Distribute Coins in Binary Tree.
Memory Usage: 12.9 MB, less than 33.33% of Python online submissions for Distribute Coins in Binary Tree.

'''
