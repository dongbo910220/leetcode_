class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        maxF = nums[0]
        minF = nums[0]
        ans = nums[0]

        for i in range(1, n):
            mx = maxF
            mn = minF
            maxF = max(mx * nums[i], nums[i], mn * nums[i])
            minF = min(mx * nums[i], nums[i], mn * nums[i])
            ans = max(ans, maxF)
        return ans