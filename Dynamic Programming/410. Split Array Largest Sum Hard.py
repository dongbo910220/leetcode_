'''
https://leetcode.com/problems/split-array-largest-sum/

Success
Details
Runtime: 4056 ms, faster than 26.68% of Python online submissions for Split Array Largest Sum.
Memory Usage: 13.1 MB, less than 21.41% of Python online submissions for Split Array Largest Sum.
'''


class Solution(object):
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        N = len(nums)

        dp = [[float('inf')] * (m + 1) for _ in range(N + 1)]

        sums = [0] * (N + 1)
        for i in range(1, N + 1):
            sums[i] = sums[i - 1] + nums[i - 1]
            dp[i][1] = sums[i]

        for i in range(1, N + 1):
            for k in range(2, m + 1):
                for j in range(k - 1, i):  #
                    dp[i][k] = min(dp[i][k], max(dp[j][k - 1], (sums[i] - sums[j])))
        # print(dp)
        return dp[N][m]