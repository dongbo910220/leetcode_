'''
Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Example:

Input:  [1,2,3,4]
Output: [24,12,8,6]
Constraint: It's guaranteed that the product of the elements of any prefix or suffix of the array (including the whole array) fits in a 32 bit integer.

Note: Please solve it without division and in O(n).

Follow up:
Could you solve it with constant space complexity? (The output array does not count as extra space for the purpose of space complexity analysis.)

'''
'''
Success
Details 
Runtime: 100 ms, faster than 90.76% of Python online submissions for Product of Array Except Self.
Memory Usage: 18 MB, less than 95.24% of Python online submissions for Product of Array Except Self.
'''


class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        output = nums
        productSum = 1
        zero_flag = 0
        for num in nums:
            if num != 0:
                productSum = productSum * num
            else:
                zero_flag += 1
        for i in range(len(nums)):
            if nums[i] == 0:
                if zero_flag == 1:
                    output[i] = productSum
                else:   # zero_flag > 1
                    output[i] = 0
            else:     # nums[i] == 0:
                if zero_flag == 0:
                    output[i] = productSum / nums[i]
                else:
                    output[i] = 0
        return output

