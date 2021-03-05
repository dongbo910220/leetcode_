'''
https://leetcode.com/problems/most-frequent-subtree-sum/

'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return None

        def dfs(node):
            if not node: return 0
            s = node.val + dfs(node.left) + dfs(node.right)
            count[s] += 1
            return s

        count = collections.Counter()
        dfs(root)
        maxCount = max(count.values())
        return [s for s in count if count[s] == maxCount]

'''
Details
Runtime: 44 ms, faster than 58.65% of Python online submissions for Most Frequent Subtree Sum.
Memory Usage: 18.7 MB, less than 77.64% of Python online submissions for Most Frequent Subtree Sum'''