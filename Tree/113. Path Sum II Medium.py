'''
Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

Note: A leaf is a node with no children.

Example:

Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \    / \
7    2  5   1
Return:

[
   [5,4,11,2],
   [5,8,4,5]
]
'''

'''
Success
Details 
Runtime: 60 ms, faster than 7.03% of Python online submissions for Path Sum II.
Memory Usage: 19 MB, less than 7.14% of Python online submissions for Path Sum II.
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if root == None:
            return []
        result = []
        current = []
        self.isPath(root, sum, result, current)
        return result

    def isPath(self, root, sum, result, current):
        # current.append(root.val)
        if root.left == None and root.right == None and root.val == sum:
            current.append(root.val)
            result.append(current)
        if root.left:
            self.isPath(root.left, sum - root.val, result, current + [root.val])
        if root.right:
            self.isPath(root.right, sum - root.val, result, current + [root.val])

