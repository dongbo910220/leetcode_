class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)

        if 1 not in nums:
            return 1

        for i in range(n):
            if nums[i] < 1 or nums[i] > n:
                nums[i] = 1

        for i in range(n):
            pos = abs(nums[i]) - 1
            nums[pos] = -abs(nums[pos])

        for i in range(n):
            if nums[i] > 0:
                return i + 1

        return n + 1