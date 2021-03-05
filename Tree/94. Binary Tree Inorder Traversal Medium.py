'''
Given a binary tree, return the inorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,3,2]
'''
'''
Success
Details 
Runtime: 20 ms, faster than 42.63% of Python online submissions for Binary Tree Inorder Traversal.
Memory Usage: 12.7 MB, less than 6.25% of Python online submissions for Binary Tree Inorder Traversal.
'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        if root == None:
            return result
        self.inorder(root, result)
        return result

    def inorder(self, root, result):
        if root.left:
            self.inorder(root.left, result)
        result.append(root.val)
        if root.right:
            self.inorder(root.right, result)
        return result

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        stack = []
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            node = stack.pop()
            result.append(node.val)
            root = node.right
        return result