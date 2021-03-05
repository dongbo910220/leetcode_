'''
https://leetcode.com/problems/remove-boxes/

Success
Details
Runtime: 1280 ms, faster than 28.13% of Python online submissions for Remove Boxes.
Memory Usage: 23.7 MB, less than 50.00% of Python online submissions for Remove Boxes.
'''


class Solution(object):
    def removeBoxes(self, boxes):
        """
        :type boxes: List[int]
        :rtype: int
        """
        n = len(boxes)
        self.boxes = boxes
        self.m = [[[0] * n for _ in xrange(n)] for _ in xrange(n)]
        return self.dfs(0, n - 1, 0)

    def dfs(self, l, r, k):
        if l > r:
            return 0
        while l < r and self.boxes[r - 1] == self.boxes[r]:
            r -= 1
            k += 1
        if self.m[l][r][k] != 0:
            return self.m[l][r][k]
        self.m[l][r][k] = self.dfs(l, r - 1, 0) + (k + 1) * (k + 1)
        for i in range(l, r):
            if self.boxes[i] == self.boxes[r]:
                self.m[l][r][k] = max(self.m[l][r][k], self.dfs(l, i, k + 1) + self.dfs(i + 1, r - 1, 0))
        return self.m[l][r][k]