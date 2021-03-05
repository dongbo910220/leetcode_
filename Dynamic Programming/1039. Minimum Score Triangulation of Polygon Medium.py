'''
https://leetcode.com/problems/minimum-score-triangulation-of-polygon/

Success
Details
Runtime: 88 ms, faster than 66.67% of Python online submissions for Minimum Score Triangulation of Polygon.
Memory Usage: 13.6 MB, less than 47.62% of Python online submissions for Minimum Score Triangulation of Polygon.
'''

class Solution(object):
    def minScoreTriangulation(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        n = len(A)
        dp = [[0] * len(A) for _ in xrange(n)]
        for l in xrange(2, n):
            for left in range(0, n - l):
                right = left + l
                dp[left][right] = float('inf')
                for mid in range(left + 1, right):
                    dp[left][right] = min(dp[left][right], dp[left][mid] + dp[mid][right] + A[left] * A[right] * A[mid])
        return dp[0][n-1]