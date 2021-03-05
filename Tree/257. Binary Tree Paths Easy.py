'''
https://leetcode.com/problems/binary-tree-paths/
'''

'''
Success
Details 
Runtime: 20 ms, faster than 61.95% of Python online submissions for Binary Tree Paths.
Memory Usage: 12.9 MB, less than 5.26% of Python online submissions for Binary Tree Paths.
'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.result = []

    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if not root:
            return self.result
        self.dfs(root, "")
        return self.result

    def dfs(self, root, S):
        if S == "":
            S += str(root.val)
        else:
            S += "->" + str(root.val)
        if not root.left and not root.right:
            self.result.append(S)
        if root.left:
            self.dfs(root.left, S)
        if root.right:
            self.dfs(root.right, S)
for i in range(2, 10):
    print(i)
print(range(2, 10))
