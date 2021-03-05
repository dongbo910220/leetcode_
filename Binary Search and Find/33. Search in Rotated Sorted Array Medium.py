'''
https://leetcode.com/problems/search-in-rotated-sorted-array/

'''


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid

            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            elif nums[left] > nums[mid]:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1

a = Solution()
print(a.search([0, 1], 1))

'''
Success
Details
Runtime: 24 ms, faster than 92.17% of Python online submissions for Search in Rotated Sorted Array.
Memory Usage: 12.9 MB, less than 98.57% of Python online submissions for Search in Rotated Sorted 

'''