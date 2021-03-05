'''
https://leetcode.com/problems/serialize-and-deserialize-binary-tree/
'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return 'x'
        return root.val, self.serialize(root.left), self.serialize(root.right)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if data[0] == 'x':
            return None
        root = TreeNode(data[0])
        root.left = self.deserialize(data[1])
        root.right = self.deserialize(data[2])
        return root