'''
https://leetcode.com/problems/maximal-square/
'''

class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix:
            return 0
        rows = len(matrix)
        cols = len(matrix[0])
        maxside = 0
        dp = [[0] * (cols + 1) for _ in range(rows+1)]
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == '1':
                    dp[i+1][j+1] = min(dp[i][j], dp[i+1][j], dp[i][j+1]) + 1
                if dp[i+1][j+1] > maxside:
                    maxside = dp[i+1][j+1]
        return maxside * maxside

'''
Success
Details 
Runtime: 156 ms, faster than 94.83% of Python online submissions for Maximal Square.
Memory Usage: 20.2 MB, less than 12.50% of Python online submissions for Maximal Square.
'''