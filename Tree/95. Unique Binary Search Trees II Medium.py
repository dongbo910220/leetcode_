'''
Given an integer n, generate all structurally unique BST's (binary search trees) that store values 1 ... n.

Example:

Input: 3
Output:
[
  [1,null,3,2],
  [3,2,null,1],
  [3,1,null,null,2],
  [2,1,3],
  [1,null,2,null,3]
]
Explanation:
The above output corresponds to the 5 unique BST's shown below:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n == 0:
            return []
        return self.generate(1, n)

    def generate(self, s, t):
        if s > t:
            return [None]
        if s == t:
            return [TreeNode(s)]
        result = []
        for i in range(s, t + 1):
            leftList = self.generate(s, i - 1)
            rightList = self.generate(i + 1, t)
            for left in leftList:
                for right in rightList:
                    root = TreeNode(i)
                    root.left = left
                    root.right = right
                    result.append(root)
        return result
