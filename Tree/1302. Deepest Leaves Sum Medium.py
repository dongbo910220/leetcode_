'''
https://leetcode.com/problems/deepest-leaves-sum/

Success
Details
Runtime: 120 ms, faster than 29.23% of Python online submissions for Deepest Leaves Sum.
Memory Usage: 20.3 MB, less than 55.09% of Python online submissions for Deepest Leaves Sum.
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def deepestLeavesSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        queue = [root]
        res = 0
        while queue:
            new_queue = []
            res = 0
            while queue:
                node = queue.pop()
                res += node.val
                if node.left:
                    new_queue.append(node.left)
                if node.right:
                    new_queue.append(node.right)
            queue = new_queue
        return res
