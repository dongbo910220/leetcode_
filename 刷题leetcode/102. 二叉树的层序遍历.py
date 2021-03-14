# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        level = [root]
        ans = []
        while level:
            new_level = []
            cur = []
            for node in level:
                cur.append(node.val)
                if node.left:
                    new_level.append(node.left)
                if node.right:
                    new_level.append(node.right)
            ans.append(cur)
            level = new_level
        return ans