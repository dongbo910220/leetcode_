'''
https://leetcode.com/problems/shortest-bridge/
'''


class Solution(object):
    def shortestBridge(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        Q = []
        n = len(A)

        def dfs(i, j):
            A[i][j] = -1
            Q.append((i, j))
            for x, y in (i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1):
                if 0 <= x < n and 0 <= y < n and A[x][y] == 1:
                    dfs(x, y)

        def first():
            for i in range(n):
                for j in range(n):
                    if A[i][j] == 1:
                        return i, j

        step = 0
        starti, startj = first()
        dfs(starti, startj)

        while Q:
            new = []
            for i, j in Q:
                for x, y in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                    if 0 <= x < n and 0 <= y < n:
                        if A[x][y] == 1:
                            return step
                        elif not A[x][y]:
                            A[x][y] = -1
                            new.append((x, y))
            step += 1
            Q = new

'''
Success
Details 
Runtime: 372 ms, faster than 90.30% of Python online submissions for Shortest Bridge.
Memory Usage: 15.6 MB, less than 47.84% of Python online submissions for Shortest Bridge.'''