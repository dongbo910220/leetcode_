'''
执行结果：
通过
显示详情
执行用时：52 ms, 在所有 Python 提交中击败了8.33% 的用户
内存消耗：17.5 MB, 在所有 Python 提交中击败了60.71% 的用户
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        def helper(node, lower=float('-inf'), upper=float('inf')):
            if not node:
                return True

            val = node.val
            if val <= lower or val >= upper:
                return False

            if not helper(node.left, lower, val):
                return False
            if not helper(node.right, val, upper):
                return False
            return True

        return helper(root)