'''
https://leetcode.com/problems/partition-equal-subset-sum/submissions/
'''

class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        N = len(nums)
        total = sum(nums)
        if total % 2 == 1:
            return False
        target = total // 2
        dp = [[False] * (target + 1) for _ in range(N)]

        if nums[0] <= target:
            dp[0][nums[0]] = True

        for i in range(1, N):
            for j in range(target + 1):
                dp[i][j] = dp[i - 1][j]
                if dp[i] == j:
                    dp[i] = True
                    continue
                if nums[i] < j:
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][j - nums[i]]
        return dp[N - 1][target]

'''
Success
Details 
Runtime: 2492 ms, faster than 20.26% of Python online submissions for Partition Equal Subset Sum.
Memory Usage: 16.5 MB, less than 37.79% of Python online submissions for Partition Equal Subset Sum.
'''