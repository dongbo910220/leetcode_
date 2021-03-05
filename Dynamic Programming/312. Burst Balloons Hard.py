'''
https://leetcode.com/problems/burst-balloons/
'''


class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        nums.insert(0, 1)
        nums.append(1)
        n1 = len(nums)
        dp = [[0] * (n1) for i in range(n1)]
        for l in range(1, n + 1):
            for i in range(1, n + 2 - l):
                j = i + l - 1
                for k in range(i, j + 1):
                    dp[i][j] = max(dp[i][j], dp[i][k - 1] + nums[i - 1] * nums[k] * nums[j + 1] + dp[k + 1][j])
        return dp[1][n]


'''
Success
Details 
Runtime: 372 ms, faster than 47.46% of Python online submissions for Burst Balloons.
Memory Usage: 13.3 MB, less than 14.29% of Python online submissions for Burst Balloons.

'''