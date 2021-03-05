'''
https://leetcode.com/problems/longest-continuous-increasing-subsequence/submissions/

Success
Details
Runtime: 52 ms, faster than 97.80% of Python online submissions for Longest Continuous Increasing Subsequence.
Memory Usage: 13.7 MB, less than 42.96% of Python online submissions for Longest Continuous Increasing Subsequence.
'''
class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        dp = [1] * len(nums)
        for i, num in enumerate(nums):
            if i == 0:
                continue
            if num > nums[i-1]:
                dp[i] = dp[i-1] + 1
        return max(dp)