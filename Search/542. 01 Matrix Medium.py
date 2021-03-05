'''
https://leetcode.com/problems/01-matrix/
'''

class Solution(object):
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        M = matrix
        Q = []
        for i, row in enumerate(matrix):
            for j, c in enumerate(row):
                if not c:
                    Q.append((i, j))
                M[i][j] *= -1
        while Q:
            newQ = []
            for i, j in Q:
                for x, y in (i-1,j),(i+1,j),(i,j-1),(i,j+1):
                    if 0<=x<len(M) and 0<=y<len(M[0]) and M[x][y]<0:
                        M[x][y] = M[i][j] + 1
                        newQ.append((x, y))
            Q = newQ
        return M
'''
Success
Details 
Runtime: 660 ms, faster than 67.95% of Python online submissions for 01 Matrix.
Memory Usage: 15.4 MB, less than 80.47% of Python online submissions for 01 Matrix.'''

class Solution(object):
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        m, n = len(matrix), len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j] != 0:
                    matrix[i][j] = float('inf')
                    if i > 0 and matrix[i - 1][j] + 1 < matrix[i][j]:
                        matrix[i][j] = matrix[i - 1][j] + 1
                    if j > 0 and matrix[i][j - 1] + 1 < matrix[i][j]:
                        matrix[i][j] = matrix[i][j - 1] + 1
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if matrix[i][j] != 0:
                    if i + 1 < m and matrix[i + 1][j] + 1 < matrix[i][j]:
                        matrix[i][j] = matrix[i + 1][j] + 1
                    if j + 1 < n and matrix[i][j + 1] + 1 < matrix[i][j]:
                        matrix[i][j] = matrix[i][j + 1] + 1
        return matrix

'''
Success
Details 
Runtime: 476 ms, faster than 98.53% of Python online submissions for 01 Matrix.
Memory Usage: 14.8 MB, less than 100.00% of Python online submissions for 01 Matrix.'''
