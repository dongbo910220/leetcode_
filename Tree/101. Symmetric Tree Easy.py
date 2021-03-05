'''
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3



But the following [1,2,2,null,3,null,3] is not:

    1
   / \
  2   2
   \   \
   3    3
'''
'''
Success
Details
Runtime: 24 ms, faster than 44.42% of Python online submissions for Symmetric Tree.
Memory Usage: 13.2 MB, less than 6.52% of Python online submissions for Symmetric Tree.

'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True
        left = root.left
        right = root.right
        return self.judgeTree(left, right)

    def judgeTree(self, left, right):
        if left == None and right == None:
            return True
        elif left != None and right == None:
            return False
        elif left == None and right != None:
            return False
        if left.val == right.val:
            return self.judgeTree(left.left, right.right) and self.judgeTree(left.right, right.left)
        else:  # left.val != right.val:
            return False
