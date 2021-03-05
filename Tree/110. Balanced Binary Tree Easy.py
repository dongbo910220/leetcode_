'''
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

a binary tree in which the left and right subtrees of every node differ in height by no more than 1.



Example 1:

Given the following tree [3,9,20,null,null,15,7]:

    3
   / \
  9  20
    /  \
   15   7
Return true.

Example 2:

Given the following tree [1,2,2,3,3,null,null,4,4]:

       1
      / \
     2   2
    / \
   3   3
  / \
 4   4
Return false.

'''

'''
Success
Details 
Runtime: 76 ms, faster than 5.48% of Python online submissions for Balanced Binary Tree.
Memory Usage: 17.4 MB, less than 6.25% of Python online submissions for Balanced Binary Tree.
'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.balance = True

    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True

        self.height(root)
        return self.balance

    def height(self, root):
        if self.balance == False:
            return -1
        if not root:
            return 0
        else:
            leftHeight = self.height(root.left)
            rightHeight = self.height(root.right)

            if abs(leftHeight - rightHeight) > 1:
                self.balance = False
                return -1

            else:
                return max(leftHeight, rightHeight) + 1