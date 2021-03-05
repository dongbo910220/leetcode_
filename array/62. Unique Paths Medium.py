'''
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?

Example 1:

Input: m = 3, n = 2
Output: 3
Explanation:
From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Right -> Down
2. Right -> Down -> Right
3. Down -> Right -> Right
Example 2:

Input: m = 7, n = 3
Output: 28
'''

# Time Limit Exceeded
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        i, j, num = 0, 0, 0
        ans = self.toDestination(m, n, i, j, num)
        return ans

    def toDestination(self, m, n, i, j, num):
        if (i == m - 1) and (j == n - 1):
            return 1
        if (i == m - 1):
            return num + self.toDestination(m, n, i, j + 1, num)
        if (j == n - 1):
            return num + self.toDestination(m, n, i + 1, j, num)
        else:
            return num + self.toDestination(m, n, i, j + 1, num) + self.toDestination(m, n, i + 1, j, num)


class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """

        if not m or not n:
            return 0
        dp = [[1 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            dp[i][0] = 1
        for j in range(n):
            dp[0][j] = 1
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[m - 1][n - 1]




# a = Solution()
# print(a.uniquePaths(7, 3))
#
# m = 7
# n = 3
# dp = [[1 for _ in range(n)] for _ in range(m)]
# # dp = [[1 for 1 in range(n)] for 1 in range(m)]
# dp[3][0] = 100
# print(dp)
#
# ds = [2 for _ in range(n)]
# print(ds)
#
# Array= [[0 for i in range(5)] for i in range(2)]
# print(Array)
