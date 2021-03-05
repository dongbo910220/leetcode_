'''
https://leetcode.com/problems/number-of-islands/submissions/
'''

from collections import deque

    def numIslands( grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0

        rows = len(grid)
        cols = len(grid[0])
        num = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':
                    self.bfs(grid, i, j)
                    num += 1
        return num

    def bfs( grid, i, j):
        queue = deque([(i, j)])
        while queue:
            x, y = queue.popleft()
            for i, j in [x + 1, y], [x - 1, y], [x, y + 1], [x, y - 1]:
                if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == '1':
                    queue.append((i, j))
                    grid[i][j] = '*'













'''
Success
Details
Runtime: 128 ms, faster than 71.82% of Python online submissions for Number of Islands.
Memory Usage: 19.9 MB, less than 18.92% of Python online submissions for Number of Islands.
'''