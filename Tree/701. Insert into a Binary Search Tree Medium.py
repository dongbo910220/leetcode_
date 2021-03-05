'''
https://leetcode.com/problems/insert-into-a-binary-search-tree/

Success
Details
Runtime: 136 ms, faster than 55.10% of Python online submissions for Insert into a Binary Search Tree.
Memory Usage: 16.9 MB, less than 25.93% of Python online submissions for Insert into a Binary Search Tree.
'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """

        def insert(node):
            if not node:
                node = TreeNode(val)
                return node
            if val < node.val:
                node.left = insert(node.left)
                return node
            else:
                node.right = insert(node.right)
                return node

        root = insert(root)
        return root