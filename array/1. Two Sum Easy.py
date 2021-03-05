'''
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

'''

'''
Success
Details 
Runtime: 32 ms, faster than 92.17% of Python online submissions for Two Sum.
Memory Usage: 13.1 MB, less than 32.53% of Python online submissions for Two Sum.

'''

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        h_dict = {}
        for i in range(len(nums)):
            if nums[i] in h_dict:
                return [h_dict[nums[i]], i]
            else:
                h_dict[target - nums[i]] = i