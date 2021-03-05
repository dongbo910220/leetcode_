'''
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
'''

import math
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        n = len(nums)
        result = []

        # [-4, -1, -1, 0, 1, 2]
        for i in range(n-2):
            if nums[i] + nums[i+1] + nums[i+2] > 0:
                break
            if nums[i] + nums[n-1] + nums[n-2] < 0:
                continue
            if (i != 0) and (nums[i-1] == nums[i]):
                continue
            l = i+1
            r = n-1
            while(l < r):
                tmp = nums[i] + nums[l] + nums[r]
                if tmp == 0:
                    result.append([nums[i], nums[l], nums[r]])
                    while(nums[l] == nums[l+1] and l+1 < r):
                        l = l + 1
                    l = l + 1
                    while(nums[r] == nums[r-1] and r-1 > l):
                        r = r - 1
                    r = r -1
                elif tmp < 0:
                    l= l+1
                else:
                    r = r-1
        return result







a = Solution()
print(a.threeSum([-1, 0, 1, 2, -1, -4]))
# print(sorted([-1, 0, 1, 2, -1, -4]))


