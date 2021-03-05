'''
https://leetcode.com/problems/as-far-from-land-as-possible/
'''

from collections import deque


class Solution(object):
    def maxDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows = len(grid)
        cols = len(grid[0])
        distance = 1
        q = deque([])
        q1 = deque([])
        maxdistance = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    q.append((i + 1, j))
                    q.append((i - 1, j))
                    q.append((i, j + 1))
                    q.append((i, j - 1))
        while q:
            distance += 1
            while q:
                i, j = q.popleft()
                if 0 <= i < rows and 0 <= j < cols and grid[i][j] == 0:
                    grid[i][j] = distance
                    maxdistance = distance
                    q1.append((i + 1, j))
                    q1.append((i - 1, j))
                    q1.append((i, j + 1))
                    q1.append((i, j - 1))
            q = q1
            q1 = deque([])

        return maxdistance - 1

'''
Success
Details 
Runtime: 552 ms, faster than 60.12% of Python online submissions for As Far from Land as Possible.
Memory Usage: 14.4 MB, less than 100.00% of Python online submissions for As Far from Land as Possible.
'''