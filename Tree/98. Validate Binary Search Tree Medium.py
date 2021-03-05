'''
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.


Example 1:

    2
   / \
  1   3

Input: [2,1,3]
Output: true
Example 2:

    5
   / \
  1   4
     / \
    3   6

Input: [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.
'''
'''
Success
Details 
Runtime: 24 ms, faster than 98.81% of Python online submissions for Validate Binary Search Tree.
Memory Usage: 17.5 MB, less than 5.66% of Python online submissions for Validate Binary Search Tree.
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
        max = float("inf")
        min = -float("inf")
        return self.valid(root, min, max)

    def valid(self, root, min, max):
        if not root:
            return True
        if root.val >= max or root.val <= min:
            return False
        if not root.left and not root.right:
            return True
        elif not root.left:
            if root.right.val > root.val:
                return self.valid(root.right, root.val, max)
            else:
                return False
        elif not root.right:
            if root.left.val < root.val:
                return self.valid(root.left, min, root.val)
            else:
                return False
        else:
            if root.left.val < root.val and root.right.val > root.val:
                return self.valid(root.right, root.val, max) and self.valid(root.left, min, root.val)
            else:
                return False


class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        max = float("inf")
        min = -float("inf")
        return self.valid(root, min, max)

    def valid(self, root, min, max):
        if not root:
            return True

        if root.val >= max or root.val <= min:
            return False

        return self.valid(root.left, min, root.val) and self.valid(root.right, root.val, max)




