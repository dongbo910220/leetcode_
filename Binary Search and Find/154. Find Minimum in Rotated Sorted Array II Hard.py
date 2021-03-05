'''
https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/

Success
Details
Runtime: 32 ms, faster than 98.14% of Python online submissions for Find Minimum in Rotated Sorted Array II.
Memory Usage: 13 MB, less than 52.50% of Python online submissions for Find Minimum in Rotated Sorted Array II.
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
            while left != mid and nums[left] == nums[mid]:
                left += 1

            if nums[mid] >= nums[left]:
                result = min(result, nums[left])
                left = mid + 1
            else:
                result = min(result, nums[mid])
                right = mid - 1
        return result