'''
https://leetcode.com/problems/minimum-difficulty-of-a-job-schedule/
'''

class Solution(object):
    def minDifficulty(self, jobDifficulty, d):
        """
        :type jobDifficulty: List[int]
        :type d: int
        :rtype: int
        """
        N = len(jobDifficulty)
        if d > N:
            return -1
        maxval = [[0] * N for _ in range(N)]
        for i in range(N):
            for j in range(i, N):
                maxval[i][j] = max(jobDifficulty[i:j+1])
        # print((float('inf') + 2))
        dp = [[float('inf')] * (d + 1) for _ in range(N +1 )]
        dp[0][0] = 0
        for i in range(1, N+1):
            for k in range(1, d+1):
                for j in range(k-1, i):
                    dp[i][k] = min(dp[i][k], dp[j][k-1] + maxval[j][i-1])
        return dp[N][d]

'''
Success
Details 
Runtime: 1464 ms, faster than 27.87% of Python online submissions for Minimum Difficulty of a Job Schedule.
Memory Usage: 13.3 MB, less than 18.03% of Python online submissions for Minimum Difficulty of a Job Schedule.
'''