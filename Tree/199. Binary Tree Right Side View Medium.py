'''https://leetcode.com/problems/binary-tree-right-side-view/'''
'''
Success
Details 
Runtime: 16 ms, faster than 85.61% of Python online submissions for Binary Tree Right Side View.
Memory Usage: 12.8 MB, less than 7.14% of Python online submissions for Binary Tree Right Side View.
'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        if not root:
            return result

        current = [root]

        while current:
            next_ = []
            for node in current:
                if node == current[-1]:
                    result.append(node.val)
                if node.left:
                    next_.append(node.left)
                if node.right:
                    next_.append(node.right)
            current = next_

        return result