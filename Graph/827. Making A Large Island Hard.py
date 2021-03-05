'''
https://leetcode.com/problems/making-a-large-island/
'''

from collections import deque


class Solution(object):
    def largestIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows = len(grid)
        cols = len(grid[0])
        color = 1
        h = dict()
        maxarea = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    color += 1
                    area = self.bfs(grid, i, j, color)
                    h[color] = area
                    if area > maxarea:
                        maxarea = area

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    area = self.getArea(grid, i, j, h)
                    if area > maxarea:
                        maxarea = area
        return maxarea

    def bfs(self, grid, i, j, color):
        area = 1
        grid[i][j] = color
        queue = deque([(i, j)])
        while queue:
            x, y = queue.popleft()
            for i, j in [x + 1, y], [x - 1, y], [x, y + 1], [x, y - 1]:
                if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == 1:
                    area += 1
                    grid[i][j] = color
                    queue.append((i, j))
        return area

    def getArea(self, grid, x, y, h):
        a = set()
        area = 1
        for i, j in [x + 1, y], [x - 1, y], [x, y + 1], [x, y - 1]:
            if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] != 0:
                color = grid[i][j]
                a.add(color)
        for c in a:
            area += h[c]
        return area
'''
Success
Details 
Runtime: 100 ms, faster than 93.33% of Python online submissions for Making A Large Island.
Memory Usage: 12.9 MB, less than 100.00% of Python online submissions for Making A Large Island.


'''