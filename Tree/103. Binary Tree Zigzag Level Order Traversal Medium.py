'''
Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:
[
  [3],
  [20,9],
  [15,7]
]
'''
'''
Success
Details 
Runtime: 20 ms, faster than 63.56% of Python online submissions for Binary Tree Zigzag Level Order Traversal.
Memory Usage: 13 MB, less than 7.14% of Python online submissions for Binary Tree Zigzag Level Order Traversal.
'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        result = []
        if root == None:
            return result
        current = [root]
        i = 0

        while current:
            current_result = []
            next_round = []
            for node in current:
                if node.left:
                    next_round.append(node.left)
                if node.right:
                    next_round.append(node.right)
                current_result.append(node.val)
            if i % 2 == 1:
                current_result = current_result[:: -1]
            i += 1
            current = next_round
            result.append(current_result)
        return result





