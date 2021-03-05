'''
https://leetcode.com/problems/delete-node-in-a-bst/

'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """

        def dfs(node, key):
            if not node:
                return None
            elif node.val < key:
                node.right = dfs(node.right, key)
            elif node.val > key:
                node.left = dfs(node.left, key)
            else:  # node.val == key:
                if not node.right:
                    return node.left
                if not node.left:
                    return node.right
                # we both have right and left
                temp = node.right
                minval = temp.val
                while temp.left:
                    temp = temp.left
                    minval = temp.val
                node.val = minval
                node.right = dfs(node.right, minval)
            return node

        return dfs(root, key)

'''
Success
Details 
Runtime: 68 ms, faster than 75.41% of Python online submissions for Delete Node in a BST.
Memory Usage: 20.8 MB, less than 82.40% of Python online submissions for Delete Node in a BST.
'''