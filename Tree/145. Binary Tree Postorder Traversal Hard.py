'''
Given a binary tree, return the postorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [3,2,1]
Follow up: Recursive solution is trivial, could you do it iteratively?

'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# result = []
# if root.left:
#     postorderTraversal(root.left)
# if root.right:
#     postorderTraversal(root.right)
# result.append(root.val)

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        if not root:
            return result
        stack = [(root, False)]
        while stack:
            root, visited = stack.pop()
            if visited:
                result.append(root.val)
            else:
                stack.append((root, True))
                if root.right:
                    stack.append((root.right, False))
                if root.left:
                    stack.append((root.left, False))

        return result
