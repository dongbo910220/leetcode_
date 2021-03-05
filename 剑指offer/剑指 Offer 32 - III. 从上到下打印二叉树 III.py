'''
剑指 Offer 32 - III. 从上到下打印二叉树 III

执行结果：
通过
显示详情
执行用时：16 ms, 在所有 Python 提交中击败了90.48% 的用户
内存消耗：13.4 MB, 在所有 Python 提交中击败了22.75% 的用户s
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root: return []
        queue = [root]
        nextLevel = []
        res = []
        order = True
        while queue:
            resLevel = []
            for node in queue:
                resLevel.append(node.val)
                if node.left:
                    nextLevel.append(node.left)
                if node.right:
                    nextLevel.append(node.right)
            if not order:
                resLevel.reverse()
            res.append(resLevel)
            order =  not order
            queue = nextLevel
            nextLevel = []
        return res