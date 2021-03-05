'''
https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
'''

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        right = len(nums) - 1
        result = nums[0]
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] >= nums[left]:
                result = min(result, nums[left])
                left = mid + 1
            else:
                result = min(result, nums[mid])
                right = mid - 1
        return result

'''
Success
Details 
Runtime: 28 ms, faster than 71.59% of Python online submissions for Find Minimum in Rotated Sorted Array.
Memory Usage: 13.1 MB, less than 17.37% of Python online submissions for Find Minimum in Rotated Sorted Array.
'''
