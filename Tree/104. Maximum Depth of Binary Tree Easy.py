'''
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its depth = 3.
'''
'''
Success
Details 
Runtime: 32 ms, faster than 50.74% of Python online submissions for Maximum Depth of Binary Tree.
Memory Usage: 15.6 MB, less than 6.17% of Python online submissions for Maximum Depth of Binary Tree.
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        if root.left == None and root.right == None:
            return 1
        else:
            return max(self.maxDepth(root.left), self.maxDepth(root.right))+1


a = [1, 2, 3]
print(a)
print(a[:: -1])
