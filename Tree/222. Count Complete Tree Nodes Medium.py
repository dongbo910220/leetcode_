'''
https://leetcode.com/problems/count-complete-tree-nodes/
'''
'''
Success
Details 
Runtime: 80 ms, faster than 62.85% of Python online submissions for Count Complete Tree Nodes.
Memory Usage: 28.8 MB, less than 5.88% of Python online submissions for Count Complete Tree Nodes.
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        result = 0
        if not root:
            return result
        current = [root]
        while current:
            next_ = []
            for node in current:
                result += 1
                if node.left:
                    next_.append(node.left)
                if node.right:
                    next_.append(node.right)
            current = next_
        return result
