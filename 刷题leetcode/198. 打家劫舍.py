class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            idx = i + 1
            dp[idx] = max(dp[idx-2] + nums[i], dp[idx-1]) if idx != 1 else nums[i]
        return max(dp)