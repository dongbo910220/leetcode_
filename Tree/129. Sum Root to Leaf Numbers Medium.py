'''
Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.

An example is the root-to-leaf path 1->2->3 which represents the number 123.

Find the total sum of all root-to-leaf numbers.

Note: A leaf is a node with no children.

Example:

Input: [1,2,3]
    1
   / \
  2   3
Output: 25
Explanation:
The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.
Therefore, sum = 12 + 13 = 25.
Example 2:

Input: [4,9,0,5,1]
    4
   / \
  9   0
 / \
5   1
Output: 1026
Explanation:
The root-to-leaf path 4->9->5 represents the number 495.
The root-to-leaf path 4->9->1 represents the number 491.
The root-to-leaf path 4->0 represents the number 40.
Therefore, sum = 495 + 491 + 40 = 1026.
'''
'''
Success
Details 
Runtime: 24 ms, faster than 27.68% of Python online submissions for Sum Root to Leaf Numbers.
Memory Usage: 12.8 MB, less than 9.09% of Python online submissions for Sum Root to Leaf Numbers.
'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.result = 0

    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        cur = 0
        self.TotalNum(root, cur)
        return self.result

    def TotalNum(self, root, cur):
        cur *= 10
        cur += root.val
        if root.left == None and root.right == None:
            self.result += cur
        if root.left:
            self.TotalNum(root.left, cur)
        if root.right:
            self.TotalNum(root.right, cur)


