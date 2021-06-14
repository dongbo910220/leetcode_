class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [0] * len(nums)
        n = len(nums)
        if n == 1:
            return nums[0]
        for i in range(0, n-1):
            if i >= 2:
                dp[i] = max(dp[i-2] + nums[i], dp[i-1])
            elif i == 1:
                dp[i] = max(nums[1], nums[0])
            elif i == 0:
                dp[i] = nums[0]
        maxval = dp[n-2]
        dp = [0] * len(nums)
        for i in range(1, n):
            if i >= 2:
                dp[i] = max(dp[i-2] + nums[i], dp[i-1])
            elif i == 1:
                dp[i] = nums[1]
        return max(maxval, dp[-1])

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def my_rob(nums):
            pre, cur = 0, 0
            for num in nums:
                cur, pre = max(pre + num, cur), cur
            return cur
        return max(my_rob(nums[:-1]), my_rob(nums[1:])) if len(nums) != 1 else nums[0]