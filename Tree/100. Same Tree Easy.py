'''
Given two binary trees, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical and the nodes have the same value.

Example 1:

Input:     1         1
          / \       / \
         2   3     2   3

        [1,2,3],   [1,2,3]

Output: true

Example 2:

Input:     1         1
          /           \
         2             2

        [1,2],     [1,null,2]

Output: false

Example 3:

Input:     1         1
          / \       / \
         2   1     1   2

        [1,2,1],   [1,1,2]

Output: false

'''
'''
Success
Details
Runtime: 12 ms, faster than 93.65% of Python online submissions for Same Tree.
Memory Usage: 12.7 MB, less than 5.00% of Python online submissions for Same Tree.
'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        return self.preorder(p, q)

    def preorder(self, p, q):
        if p == None and q == None:
            return True
        elif p == None and q != None:
            return False
        elif p != None and q == None:
            return False
        elif p.val == q.val:
            return self.preorder(p.left, q.left) and self.preorder(p.right, q.right)
        else:  # p.val != q.val:
            return False



