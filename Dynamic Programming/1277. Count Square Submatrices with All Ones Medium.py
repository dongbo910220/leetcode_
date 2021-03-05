'''
https://leetcode.com/problems/count-square-submatrices-with-all-ones/

Success
Details
Runtime: 824 ms, faster than 28.79% of Python online submissions for Count Square Submatrices with All Ones.
Memory Usage: 14.8 MB, less than 30.30% of Python online submissions for Count Square Submatrices with All Ones.
'''

class Solution(object):
    def countSquares(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        if matrix is None or len(matrix) == 0:
            return 0

        rows = len(matrix)
        cols = len(matrix[0])

        result = 0

        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 1:
                    if r == 0 or c == 0:
                        result += 1
                    else:
                        cell_val = min(matrix[ r -1][ c -1], matrix[r][ c -1], matrix[ r -1][c]) + matrix[r][c]
                        result += cell_val
                        matrix[r][c] = cell_val
        return result