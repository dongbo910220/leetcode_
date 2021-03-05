'''
https://leetcode.com/problems/out-of-boundary-paths/
'''


class Solution(object):
    def findPaths(self, m, n, N, i, j):
        """
        :type m: int
        :type n: int
        :type N: int
        :type i: int
        :type j: int
        :rtype: int
        """
        MOD = 10 ** 9 + 7
        directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]
        next = [[0] * n for _ in range(m)]
        next[i][j] = 1

        ans = 0
        for time in range(N):
            cur = next
            next = [[0] * n for _ in range(m)]
            for r, row in enumerate(cur):
                for c, val in enumerate(row):
                    for nr, nc in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
                        if 0 <= nr < m and 0 <= nc < n:
                            next[nr][nc] += val
                            next[nr][nc] %= MOD
                        else:
                            ans += val
                            ans %= MOD
        return ans

'''
Success
Details 
Runtime: 344 ms, faster than 29.52% of Python online submissions for Out of Boundary Paths.
Memory Usage: 12.8 MB, less than 85.71% of Python online submissions for Out of Boundary Paths.
'''