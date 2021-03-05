'''
https://leetcode.com/problems/minimum-absolute-difference-in-bst/
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        nums = self.inorder(root)
        return min([nums[i + 1] - nums[i] for i in range(len(nums) - 1)])

    def inorder(self, node):
        return self.inorder(node.left) + [node.val] + self.inorder(node.right) if node else []


'''
Success
Details 
Runtime: 56 ms, faster than 36.33% of Python online submissions for Minimum Absolute Difference in BST.
Memory Usage: 16.8 MB, less than 74.50% of Python online submissions for Minimum Absolute Difference in BST.'''