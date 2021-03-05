'''
https://leetcode.com/problems/cherry-pickup/

超时
正确版本在最后
Success
Details
Runtime: 776 ms, faster than 58.10% of Python online submissions for Cherry Pickup.
Memory Usage: 15.2 MB, less than 84.76% of Python online submissions for Cherry Pickup
'''

#超时 edition
class Solution(object):
    def cherryPickup(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        self.m_ = [[[-(float('inf'))] * n for _ in range(n)] for _ in range(n)]
        return max(0, self.helper(n - 1, n - 1, n - 1, grid))

    def helper(self, x1, y1, x2, grid):
        y2 = x1 + y1 - x2
        if x1 < 0 or y1 < 0 or x2 < 0 or y2 < 0:
            return -1
        if grid[x1][y1] < 0 or grid[x2][y2] < 0:
            return -1
        if x1 == 0 and y1 == 0:
            return grid[x1][y1]
        if self.m_[x1][y1][x2] != -float('inf'):
            return self.m_[x1][y1][x2]
        ans = max(self.helper(x1 - 1, y1, x2 - 1, grid), self.helper(x1, y1 - 1, x2 - 1, grid),
                  self.helper(x1 - 1, y1, x2, grid), self.helper(x1, y1 - 1, x2, grid))
        if ans < 0:
            return -1
        ans += grid[x1][y1]
        if x1 != x2:
            ans += grid[x2][y2]
        self.m_[x1][y1][x2] = ans
        return self.m_[x1][y1][x2]


'''
正确版本

'''
class Solution(object):
    def cherryPickup(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        self.m_ = [[[-(float('inf'))] * n for _ in range(n)] for _ in range(n)]
        return max(0, self.helper(n - 1, n - 1, n - 1, grid))

    def helper(self, x1, y1, x2, grid):
        y2 = x1 + y1 - x2
        if x1 < 0 or y1 < 0 or x2 < 0 or y2 < 0:
            return -1
        if grid[x1][y1] < 0 or grid[x2][y2] < 0:
            return -1
        if x1 == 0 and y1 == 0:
            return grid[x1][y1]
        if self.m_[x1][y1][x2] != -float('inf'):
            return self.m_[x1][y1][x2]
        ans = max(self.helper(x1 - 1, y1, x2 - 1, grid), self.helper(x1, y1 - 1, x2 - 1, grid),
                  self.helper(x1 - 1, y1, x2, grid), self.helper(x1, y1 - 1, x2, grid))
        # difference is here
        if ans < 0:
            self.m_[x1][y1][x2] = -1
            return -1
        ans += grid[x1][y1]
        if x1 != x2:
            ans += grid[x2][y2]
        self.m_[x1][y1][x2] = ans
        return self.m_[x1][y1][x2]