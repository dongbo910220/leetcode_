'''
https://leetcode.com/problems/delete-leaves-with-a-given-value/submissions/

Success
Details
Runtime: 40 ms, faster than 89.12% of Python online submissions for Delete Leaves With a Given Value.
Memory Usage: 13.8 MB, less than 13.78% of Python online submissions for Delete Leaves With a Given Value.
'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def removeLeafNodes(self, root, target):
        """
        :type root: TreeNode
        :type target: int
        :rtype: TreeNode
        """

        def dfs(s):
            if not s:
                return True
            # if s.val != target:
            #     return False
            isLeft = dfs(s.left)
            if isLeft:
                s.left = None
            isRight = dfs(s.right)
            if isRight:
                s.right = None
            if s.val == target and isLeft and isRight:  # s.val == target
                return True
            else:
                return False

        dummy = TreeNode()
        dummy.right = root
        dfs(dummy)
        return dummy.right