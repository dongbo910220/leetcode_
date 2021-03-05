'''
https://leetcode.com/problems/house-robber-ii/submissions/
'''


class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        result1 = self.robInLine(nums[1:])
        result2 = self.robInLine(nums[:-1])
        return max(result1, result2)

    def robInLine(self, nums):
        n = len(nums)
        amount = [0] * (n + 2)
        for i in range(n):
            amount[i + 2] = max(amount[i + 1], nums[i] + amount[i])

        return amount[n + 1]

'''
经提醒做出
Success
Details 
Runtime: 12 ms, faster than 96.87% of Python online submissions for House Robber II.
Memory Usage: 12.9 MB, less than 11.11% of Python online submissions for House Robber II.

'''

# print([0] * 2)
# print(max([2, 1]))
# print(max([2, 1]))