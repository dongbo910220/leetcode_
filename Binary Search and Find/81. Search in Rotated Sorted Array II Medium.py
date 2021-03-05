'''
https://leetcode.com/problems/search-in-rotated-sorted-array-ii/
'''

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        left = 0
        right = len(nums) - 1
        while left <= right:

            mid = (left + right) // 2

            if nums[mid] == target:
                return True
            while left < mid and nums[left] == nums[mid]:
                left += 1

            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return False

'''
Success
Details 
Runtime: 32 ms, faster than 97.63% of Python online submissions for Search in Rotated Sorted Array II.
Memory Usage: 13 MB, less than 46.61% of Python online submissions for Search in Rotated Sorted Array II.
'''
