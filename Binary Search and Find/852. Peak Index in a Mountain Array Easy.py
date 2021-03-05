'''
https://leetcode.com/problems/peak-index-in-a-mountain-array/

Success
Details
Runtime: 60 ms, faster than 83.23% of Python online submissions for Peak Index in a Mountain Array.
Memory Usage: 13.6 MB, less than 91.64% of Python online submissions for Peak Index in a Mountain Array.
'''


class Solution(object):
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        nums = A
        left = 0
        right = len(nums) - 1
        n = right

        while left <= right:
            mid = (left + right) // 2
            if mid == 0:
                if nums[mid] > nums[1]:
                    return 0
                else:
                    return 1
            if mid == n:
                if nums[mid] > nums[mid - 1]:
                    return mid
            else:  # mid != 0 or n
                if nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]:
                    return mid
                else:
                    if nums[mid] < nums[mid - 1]:
                        right = mid - 1
                    elif nums[mid] < nums[mid + 1]:
                        left = mid + 1