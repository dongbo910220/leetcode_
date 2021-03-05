'''
https://leetcode.com/problems/shortest-path-to-get-all-keys/
'''


class Solution(object):
    def shortestPathAllKeys(self, grid):
        """
        :type grid: List[str]
        :rtype: int
        """
        n, m = len(grid), len(grid[0])
        numOfKeys = 0
        direc = [[0, 1], [0, -1], [-1, 0], [1, 0]]
        moves = set()

        for i in range(n):
            for j in range(m):
                if grid[i][j] == '@':
                    starti = i
                    startj = j
                elif grid[i][j] in 'abcdef':
                    numOfKeys += 1

        queue = collections.deque()
        queue.append([starti, startj, 0, ".@abcdef", 0])

        while queue:
            i, j, steps, keys, collectedKeys = queue.popleft()

            if grid[i][j] in "abcdef" and grid[i][j].upper() not in keys:
                keys += grid[i][j].upper()
                collectedKeys += 1

            if collectedKeys == numOfKeys:
                return steps

            for x, y in direc:
                ni = i + x
                nj = j + y
                if 0 <= ni < n and 0 <= nj < m and grid[ni][nj] in keys:
                    if (ni, nj, keys) not in moves:
                        moves.add((ni, nj, keys))
                        queue.append([ni, nj, steps + 1, keys, collectedKeys])
        return -1


'''
Success
Details 
Runtime: 720 ms, faster than 28.13% of Python online submissions for Shortest Path to Get All Keys.
Memory Usage: 21.5 MB, less than 100.00% of Python online submissions for Shortest Path to Get All Keys.'''