'''
https://leetcode.com/problems/target-sum/
'''


# class Solution(object):
#     def findTargetSumWays(self, nums, S):
#         """
#         :type nums: List[int]
#         :type S: int
#         :rtype: int
#         """
#         index = len(nums) - 1
#         cur_sum = 0
#         self.memo = {}
#         return self.dp(nums, S, index, cur_sum)
#
#     def dp(self, nums, target, index, cur_sum):
#         if (index, cur_sum) in self.memo:
#             return self.memo[(index, cur_sum)]
#
#         if index < 0 and cur_sum == target:
#             return 1
#         if index < 0:
#             return 0
#
#         positive = self.dp(nums, target, index - 1, cur_sum + nums[index])
#         negative = self.dp(nums, target, index - 1, cur_sum - nums[index])
#
#         self.memo[(index, cur_sum)] = positive + negative
#         return self.memo[(index, cur_sum)]

'''
Success
Details 
Runtime: 428 ms, faster than 40.88% of Python online submissions for Target Sum.
Memory Usage: 13.1 MB, less than 48.07% of Python online submissions for Target Sum.'''


class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        total = sum(nums)
        if (S + total) % 2 == 1:
            return 0
        if S > total:
            return 0

        target = (S + total) // 2
        print(target)
        dp = [0] * (target + 1)
        dp[0] = 1
        for num in nums:
            for i in range(target, num - 1, -1):
                if i < num:
                    continue
                else:
                    dp[i] += dp[i - num]
        print(dp)
        return dp[target]

a = Solution()
print(a.findTargetSumWays([1,1,1,1,1] ,3))


class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        total = sum(nums)
        if (S + total) % 2 == 1:
            return 0
        if S > total:
            return 0

        target = (S + total) // 2
        print(target)
        dp = [[0 for _ in range(target + 1)] for _ in range(len(nums) + 1)]
        dp[0][0] = 1
        for i in range(1, len(nums) + 1):
            for j in range(target + 1):
                if j < nums[i - 1]:
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j] + dp[i - 1][j - nums[i - 1]]
        return dp[len(nums)][target]










