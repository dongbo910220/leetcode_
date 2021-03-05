'''
Given inorder and postorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]
Return the following binary tree:

    3
   / \
  9  20
    /  \
   15   7
'''
'''
Success
Details 
Runtime: 184 ms, faster than 26.29% of Python online submissions for Construct Binary Tree from Inorder and Postorder Traversal.
Memory Usage: 87.1 MB, less than 7.14% of Python online submissions for Construct Binary Tree from Inorder and Postorder Traversal.
'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if not inorder or not postorder:
            return None

        root_val = postorder[-1]
        root = TreeNode(root_val)
        postorder.pop()

        inorder_idx = inorder.index(root_val)

        root.left = self.buildTree(inorder[:inorder_idx], postorder[:inorder_idx])
        root.right = self.buildTree(inorder[inorder_idx + 1:], postorder[inorder_idx:])

        return rootGiven a binary tree, flatten it to a linked list in-place.

For example, given the following tree:

    1
   / \
  2   5
 / \   \
3   4   6
The flattened tree should look like:

1
 \
  2
   \
    3
     \
      4
       \
        5
         \
          6
Accepted
311,710
Submissions
663,268

