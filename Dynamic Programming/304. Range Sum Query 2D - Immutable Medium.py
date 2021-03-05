'''
https://leetcode.com/problems/range-sum-query-2d-immutable/
'''

'''
Success
Details 
Runtime: 192 ms, faster than 17.34% of Python online submissions for Range Sum Query 2D - Immutable.
Memory Usage: 15.5 MB, less than 14.29% of Python online submissions for Range Sum Query 2D - Immutable.'''



class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        if matrix:
            rows = len(matrix)
            cols = len(matrix[0])
            self.dp = [[0] * cols for i in range(rows)]
            for i in range(rows):
                self.dp[i][0] = matrix[i][0]
                for j in range(1, cols):
                    self.dp[i][j] = self.dp[i][j - 1] + matrix[i][j]
        else:
            self.dp = []

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        if not self.dp:
            return 0
        res = 0
        for i in range(row1, row2 + 1):
            if col1 == 0:
                res += self.dp[i][col2]
            else:
                res += self.dp[i][col2] - self.dp[i][col1 - 1]
        return res
