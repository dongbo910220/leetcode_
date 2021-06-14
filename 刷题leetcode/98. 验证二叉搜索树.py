# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def isBST(node, lower, upper):
            print(lower, upper)
            if not node:
                return True
            val = node.val
            if lower != None and val <= lower:
                return False
            if upper != None and val >= upper:
                return False
            if  not isBST(node.left, lower, val):
                return False
            if  not isBST(node.right, val, upper):
                return False
            return True
        return isBST(root, None, None)


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def isBST(node):
            if not node:
                return True
            if not isBST(node.left):
                return False
            if node.val <= self.pre:
                print(node.val)
                print(self.pre)
                return False
            self.pre = node.val
            return isBST(node.right)
        self.pre = -float('inf')
        return isBST(root)



