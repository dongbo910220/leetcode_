'''
https://leetcode.com/problems/recover-binary-search-tree/
'''


class Solution(object):
    def inorder(self, root, result):
        if not root:
            return
        self.inorder(root.left, result)
        result.append(root)
        self.inorder(root.right, result)

    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        result = []
        parent = []
        self.inorder(root, result)
        i = 0
        pairs = []
        while (i < len(result) - 1):
            if result[i].val > result[i + 1].val:
                pairs.append([i, i + 1])
            i += 1
        if len(pairs) == 2:
            first_idx = pairs[0][0]
            second_idx = pairs[1][1]
        if len(pairs) == 1:
            first_idx, second_idx = pairs[0]

        result[first_idx].val, result[second_idx].val = result[second_idx].val, result[first_idx].val
        return root

total = 0
a = [5,4,8,11,13,4,7,2,1]
for num in a:
    total += num

print(total)
'''
Details 
Runtime: 56 ms, faster than 88.12% of Python online submissions for Recover Binary Search Tree.
Memory Usage: 13.2 MB, less than 14.29% of Python online submissions for Recover Binary Search Tree.

'''