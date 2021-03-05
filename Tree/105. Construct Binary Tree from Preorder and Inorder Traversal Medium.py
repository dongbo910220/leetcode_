'''
Given preorder and inorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
Return the following binary tree:

    3
   / \
  9  20
    /  \
   15   7

'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not preorder or not inorder:
            return None

        rootValue = preorder[0]
        root = ListNode(rootValue)
        inorder_idx = inorder.index(rootValue)

        root.left = self.buildTree(preorder[1:inorder_idx + 1], inorder[:inorder_idx])
        root.right = self.buildTree(preorder[inorder_idx + 1:], inorder[inorder_idx + 1:])

        return root