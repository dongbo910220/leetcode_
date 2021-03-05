'''
https://leetcode.com/problems/house-robber-iii/
'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        result = self.helper(root)
        return max(result)

    def helper(self, root):
        if not root:
            return [0] * 2
        # [0 1] 0 present keep the house 1 present stole the house
        a = [0] * 2
        left = self.helper(root.left)
        right = self.helper(root.right)
        a[0] = max(left) + max(right)
        a[1] = left[0] + right[0] + root.val
        return a

'''
经提醒做出
Success
Details 
Runtime: 32 ms, faster than 94.52% of Python online submissions for House Robber III.
Memory Usage: 16.8 MB, less than 14.29% of Python online submissions for House Robber III.
'''

