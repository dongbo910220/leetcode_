class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        dp = [-1] * n
        dp[0] = 1
        longest = 0
        for i, num in enumerate(nums):
            if dp[i] == 1 and i + num >= longest:
                j = longest
                longest = i + num
                while j <= longest and j <= n - 1:
                    dp[j] = 1
                    j += 1

        print(dp)
        return dp[-1] == 1

class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        longest = 0
        for i, num in enumerate(nums):
            if i > longest:
                return False
            longest = max(i + num, longest)
        return True