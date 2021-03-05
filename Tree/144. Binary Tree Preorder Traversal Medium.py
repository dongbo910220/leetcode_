'''
Given a binary tree, return the preorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,2,3]
Follow up: Recursive solution is trivial, could you do it iteratively?

'''
'''
Success
Details 
Runtime: 12 ms, faster than 94.76% of Python online submissions for Binary Tree Preorder Traversal.
Memory Usage: 12.7 MB, less than 5.72% of Python online submissions for Binary Tree Preorder Traversal.
'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# result = []
# result.append(root.val)
# if root.left:
#     postorderTraversal(root.left)
# if root.right:
#     postorderTraversal(root.right)
#

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        List = [root]
        result = []
        while List:
            node = List.pop()
            result.append(node.val)
            if node.right:
                List.append(node.right)
            if node.left:
                List.append(node.left)

        return result
