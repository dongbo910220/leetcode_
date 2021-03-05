'''
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Example:

Input:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
Output: 7
Explanation: Because the path 1→3→1→1→1 minimizes the sum.
'''


class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        start_i = 0
        start_j = 0
        min_sum = self.goThePath(grid, start_i, start_j)
        return min_sum

    def goThePath(self, grid, i, j):
        if (i == len(grid) - 1) and (j == len(grid[i]) - 1):
            return grid[i][j]
        if (i == len(grid) - 1):
            return grid[i][j] + self.goThePath(grid, i, j + 1)
        if (j == len(grid[i]) - 1):
            return grid[i][j] + self.goThePath(grid, i + 1, j)
        else:
            return grid[i][j] + min(self.goThePath(grid, i, j + 1), self.goThePath(grid, i + 1, j))

class Solution_1(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        matrix = [[None for _ in range(n)] for _ in range(m)]
        print(matrix)
        matrix[0][0] = grid[0][0]
        for i in range(1, m):
            matrix[i][0] = matrix[i - 1][0] + grid[i][0]
        for j in range(1, n):
            matrix[0][j] = matrix[0][j - 1] + grid[0][j]
        for i in range(1, m):
            for j in range(1, n):
                matrix[i][j] = grid[i][j] + min(matrix[i-1][j], matrix[i][j - 1])
        return matrix[m-1][n-1]


a = Solution_1()
print(a.minPathSum([
  [1,3,1],
  [1,5,1],
  [4,2,1]
]))