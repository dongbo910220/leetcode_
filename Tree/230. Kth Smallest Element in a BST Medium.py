'''
https://leetcode.com/problems/kth-smallest-element-in-a-bst/
'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# inorder:
#     inorder(tree.left)
#     print(tree.val)
#     inorder(tree.right)

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        List = []
        self.inorderTraversalTree(root, List)
        return List[(k - 1)]

    def inorderTraversalTree(self, root, List):
        if not root:
            return
        self.inorderTraversalTree(root.left, List)
        List.append(root.val)
        self.inorderTraversalTree(root.right, List)
