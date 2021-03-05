'''
https://leetcode.com/problems/max-area-of-island/submissions/
'''

'''
Success
Details 
Runtime: 120 ms, faster than 80.53% of Python online submissions for Max Area of Island.
Memory Usage: 12.7 MB, less than 82.35% of Python online submissions for Max Area of Island.
'''

from collections import deque


class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return 0

        num = 0
        maxsize = 0
        size = 0
        rows = len(grid)
        cols = len(grid[0])
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    grid[i][j] = 0
                    num += 1
                    size = self.bfs(grid, i, j)
                    if size > maxsize:
                        maxsize = size
        return maxsize

    def bfs(self, grid, i, j):
        queue = deque([(i, j)])
        size = 1
        while queue:
            x, y = queue.popleft()
            for i, j in [x + 1, y], [x - 1, y], [x, y + 1], [x, y - 1]:
                if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == 1:
                    grid[i][j] = '*'
                    queue.append((i, j))
                    size += 1
        return size