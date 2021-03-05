'''
https://leetcode.com/problems/largest-sum-of-averages/
'''


class Solution(object):
    def largestSumOfAverages(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: float
        """
        N = len(A)
        dp = [[0.0] * (N + 1) for _ in range(K + 1)]
        sums = [0.0] * (N + 1)
        # print(5 / (2 * 1.0))
        for i in range(1, N + 1):
            sums[i] = sums[i - 1] + A[i - 1]
            dp[1][i] = sums[i] / (i * 1.0)

        for k in range(2, K + 1):
            for i in range(k, N + 1):  # ...j... i
                for j in range(k - 1, i):
                    dp[k][i] = max(dp[k][i], dp[k - 1][j] + (sums[i] - sums[j]) / (i - j * 1.0))
        # print(dp)
        return dp[K][N]

'''
Success
Details 
Runtime: 244 ms, faster than 84.75% of Python online submissions for Largest Sum of Averages.
Memory Usage: 12.8 MB, less than 94.07% of Python online submissions for Largest Sum of Averages.
'''