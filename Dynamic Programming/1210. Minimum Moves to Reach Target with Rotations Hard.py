'''
https://leetcode.com/problems/minimum-moves-to-reach-target-with-rotations/


'''


class Solution(object):
    def minimumMoves(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        start = (0, 0, 0, 1)
        end = (n-1, n-2, n-1, n-1)
        cur_level = {start}
        moves = 0
        visited = set()
        while cur_level:
            next_level = set()
            for pos in cur_level:
                visited.add(pos)
                r1, c1, r2, c2 = pos
                if c1 + 1 < n and  c2 + 1 < n and grid[r1][c1+1] == 0 and grid[r2][c2+1] == 0:
                    if (r1, c1+1, r2, c2+1) not in visited:
                        next_level.add((r1, c1+1, r2, c2+1))
                if r1 + 1 < n and  r2 + 1 < n and grid[r1+1][c1] == 0 and grid[r2+1][c2] == 0:
                    if (r1+1, c1, r2+1, c2) not in visited:
                        next_level.add((r1+1, c1, r2+1, c2))
                if r1 == r2 and c2 == c1 + 1 and r1 + 1 < n and grid[r1+1][c1] + grid[r2+1][c2] == 0:
                    if (r1, c1, r2+1, c2-1) not in visited:
                        next_level.add((r1, c1, r2+1, c2-1))
                if c1 == c2 and r2 == r1 + 1 and c1 + 1 < n and grid[r1][c1+1] + grid[r2][c2+1] == 0:
                    if (r1, c1, r2-1, c2 + 1) not in visited:
                        next_level.add((r1, c1, r2-1, c2 + 1))
            cur_level = next_level
            moves += 1
            if end in next_level:
                return moves
        return -1


