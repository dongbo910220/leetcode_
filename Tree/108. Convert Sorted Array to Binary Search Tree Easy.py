'''
Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example:

Given the sorted array: [-10,-3,0,5,9],

One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

      0
     / \
   -3   9
   /   /
 -10  5
'''
'''
Success
Details 
Runtime: 56 ms, faster than 92.54% of Python online submissions for Convert Sorted Array to Binary Search Tree.
Memory Usage: 16.9 MB, less than 9.09% of Python online submissions for Convert Sorted Array to Binary Search Tree.
'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        n = len(nums)
        mid = n // 2
        r = n - 1
        l = 0
        return self.generateTree(l, r, nums)

    def generateTree(self, l, r, nums):
        if l <= r:
            mid = (r + l) // 2
            node = ListNode(nums[mid])
            node.left = self.generateTree(l, mid - 1, nums)
            node.right = self.generateTree(mid + 1, r, nums)
            return node
        else:  # l > r
            return None


