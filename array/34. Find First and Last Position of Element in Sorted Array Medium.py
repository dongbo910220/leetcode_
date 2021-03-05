'''
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
'''

# 超时
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(nums) - 1
        l_id = -1
        r_id = -1
        left = 0
        right = len(nums) - 1
        while (left <= right):
            if n == 0 and nums[left] == target:
                return [0, 0]
            if n == 1:
                if (nums[left] == target):
                    if (nums[right] == target):
                        return [0, 1]
                    else:
                        return [0, 0]
                if (nums[right] == target):
                    return [1, 1]
            mid = (left + right) // 2
            if (nums[mid] == target):
                l_id = r_id = mid
                if mid != 0:
                    while (nums[l_id] == target):
                        if (l_id != 0):
                            l_id -= 1
                    if (nums[l_id] != target):
                        l_id += 1
                else:
                    l_id = 0
                if mid != n:
                    while (nums[r_id] == target):
                        if (r_id != n):
                            r_id += 1
                    if (nums[r_id] != target):
                        r_id -= 1
                else:
                    r_id = n
                return [l_id, r_id]
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return [-1, -1]


class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        def binarySearchLeft(nums, target):
            l = 0
            r = len(nums) - 1
            while (l < r):
                mid = (l + r) // 2
                if target <= nums[mid]:
                    r = mid
                else:
                    l = mid + 1
            if nums[l] != target:
                l = -1
            return l

        def binarySearchRight(nums, target):
            l = 0
            r = len(nums) - 1
            while (l < r):
                mid = (l + r) // 2 + 1
                if target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid
            if nums[r] != target:
                r = -1
            return r

        if (len(nums) == 0):
            return [-1, -1]
        l, r = binarySearchLeft(nums, target), binarySearchRight(nums, target)
        if l == -1:
            return [-1, -1]
        else:
            return [l, r]








