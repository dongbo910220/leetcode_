'''
https://leetcode.com/problems/unique-paths-iii/
'''


class Solution(object):
    def uniquePathsIII(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        T = grid
        m = len(grid)
        n = len(grid[0])
        num = 1  # 终点
        for i in range(m):
            for j in range(n):
                if T[i][j] == 0:
                    num += 1
                if T[i][j] == 1:
                    starti = i
                    startj = j
                    T[i][j] = 0
        return self.dfs(T, starti, startj, num)

    def dfs(self, T, i, j, num):
        if i < 0 or j < 0 or i >= len(T) or j >= len(T[0]):
            return 0
        if T[i][j] == 1:
            return 0
        if T[i][j] == -1:
            return 0
        if T[i][j] == 2:
            return num == 0
        T[i][j] = -1
        path = self.dfs(T, i + 1, j, num - 1) + \
               self.dfs(T, i - 1, j, num - 1) + \
               self.dfs(T, i, j + 1, num - 1) + \
               self.dfs(T, i, j - 1, num - 1)
        T[i][j] = 0
        return path

'''
Success
Details 
Runtime: 36 ms, faster than 90.19% of Python online submissions for Unique Paths III.
Memory Usage: 12.7 MB, less than 33.33% of Python online submissions for Unique Paths III.
'''