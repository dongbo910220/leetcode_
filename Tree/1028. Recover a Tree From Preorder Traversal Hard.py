'''
https://leetcode.com/problems/recover-a-tree-from-preorder-traversal/
'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def recoverFromPreorder(self, S):
        """
        :type S: str
        :rtype: TreeNode
        """
        stack = []
        i = 0
        while i < len(S):
            level = 0
            val = ''
            while i < len(S) and S[i] == '-':
                i += 1
                level += 1
            while i < len(S) and S[i] != '-':
                val += S[i]
                i += 1
            node = TreeNode(val)
            while len(stack) > level:
                stack.pop()
            if not stack:
                stack.append(node)
            else:
                lastNode = stack[-1]
                if not lastNode.left:
                    lastNode.left = node
                else:
                    lastNode.right = node
                stack.append(node)
        return stack[0]

'''
Success
Details 
Runtime: 72 ms, faster than 84.21% of Python online submissions for Recover a Tree From Preorder Traversal.
Memory Usage: 13.6 MB, less than 100.00% of Python online submissions for Recover a Tree From Preorder Traversal.
'''
