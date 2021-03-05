'''
https://leetcode.com/problems/unique-paths-ii/
'''
'''
Success
Details 
Runtime: 36 ms, faster than 39.29% of Python online submissions for Unique Paths II.
Memory Usage: 12.7 MB, less than 5.26% of Python online submissions for Unique Paths II.
'''

class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        dp = obstacleGrid
        n1 = len(dp)  # 行
        n2 = len(dp[0])  # 列
        for i in range(n1):
            for j in range(n2):
                if dp[i][j] == 1:
                    dp[i][j] = '*'
        for j in range(n2):
            if dp[0][j] == '*':
                break
            else:
                dp[0][j] = 1
        for i in range(n1):
            if dp[i][0] == '*':
                break
            else:
                dp[i][0] = 1
        # print("n1", n1)
        for i in range(1, n1):
            for j in range(1, n2):
                if dp[i][j] == '*':
                    continue
                if dp[i - 1][j] != "*" and dp[i][j - 1] != "*":
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
                elif dp[i - 1][j] == "*" and dp[i][j - 1] != "*":
                    dp[i][j] = dp[i][j - 1]
                elif dp[i - 1][j] != "*" and dp[i][j - 1] == "*":
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = '*'

        # print(dp[0])
        # print(dp[1])
        # print(dp[2])

        if dp[n1 - 1][n2 - 1] == '*':
            return 0
        else:
            return dp[n1 - 1][n2 - 1]