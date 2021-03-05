'''
https://leetcode.com/problems/path-sum-iii/

'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        target = sum
        self.numOfPaths = 0
        self.dfs(root, target)
        return self.numOfPaths

    def dfs(self, node, target):
        if node is None:
            return
        self.test(node, target)
        self.dfs(node.left, target)
        self.dfs(node.right, target)

    def test(self, node, target):
        if node is None:
            return
        if node.val == target:
            self.numOfPaths += 1
        self.test(node.left, target - node.val)
        self.test(node.right, target - node.val)

'''
Success
Details
Runtime: 1160 ms, faster than 8.91% of Python online submissions for Path Sum III.
Memory Usage: 13.8 MB, less than 82.33% of Python online submissions for Path Sum III.
'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        self.result = 0
        target = sum
        cache = {0: 1}
        self.dfs(root, target, 0, cache)
        return self.result

    def dfs(self, root, target, currPathSum, cache):
        if root is None:
            return
        currPathSum += root.val
        oldPathSum = currPathSum - target
        self.result += cache.get(oldPathSum, 0)
        cache[currPathSum] = cache.get(currPathSum, 0) + 1

        self.dfs(root.left, target, currPathSum, cache)
        self.dfs(root.right, target, currPathSum, cache)

        cache[currPathSum] -= 1