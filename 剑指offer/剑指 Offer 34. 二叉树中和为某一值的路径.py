a = [1,2,3]
print(a)
# print(a + 3)
print(a + [1,2])
a.append(6)
print(a)

'''
执行结果：
通过
显示详情
执行用时：28 ms, 在所有 Python 提交中击败了85.66% 的用户
内存消耗：19 MB, 在所有 Python 提交中击败了13.32% 的用户'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if not root:
            return []
        current = []
        result = []
        self.isPath(root, sum, result, current)
        return result

    def isPath(self, root, rest, res, current):
        if not root.left and not root.right and root.val == rest:
            # current.append(root.val)
            res.append(current + [root.val])
        if root.left:
            self.isPath(root.left, rest - root.val, res, current + [root.val])
        if root.right:
            self.isPath(root.right, rest - root.val, res, current + [root.val])
