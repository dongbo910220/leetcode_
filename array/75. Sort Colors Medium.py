'''
Given an array with n objects colored red, white or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note: You are not suppose to use the library's sort function for this problem.

Example:

Input: [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
Follow up:

A rather straight forward solution is a two-pass algorithm using counting sort.
First, iterate the array counting number of 0's, 1's, and 2's, then overwrite array with total number of 0's, then 1's and followed by 2's.
Could you come up with a one-pass algorithm using only constant space?



'''
'''
Success
Details 
Runtime: 12 ms, faster than 96.84% of Python online submissions for Sort Colors.
Memory Usage: 11.9 MB, less than 20.51% of Python online submissions for Sort Colors.'''

class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        zero_idx = -1
        one_idx = -1
        two_idx = -1
        for i in range(len(nums)):
            if i == 0:
                if nums[0] == 0:
                    zero_idx = 0
                if nums[0] == 1:
                    one_idx = 0
                if nums[0] == 2:
                    two_idx = 0
            else:
                if nums[i] >= nums[i - 1]:
                    if nums[i] == 1:
                        one_idx = i
                    if nums[i] == 2:
                        two_idx = i
                    if nums[i] == 0:
                        zero_idx = i
                else:
                    if nums[i] == 0:
                        if nums[i - 1] == 1:
                            if zero_idx != -1:
                                zero_idx += 1
                                nums[i], nums[zero_idx] = nums[zero_idx], nums[i]
                            else:
                                zero_idx += 1
                                nums[i], nums[zero_idx] = nums[zero_idx], nums[i]
                            one_idx = i
                        if nums[i - 1] == 2:
                            if one_idx == -1:
                                # print("call me one_idx == -1")
                                zero_idx += 1
                                nums[i], nums[zero_idx] = nums[zero_idx], nums[i]
                                two_idx = i
                            else:
                                # print("call me now")
                                one_idx += 1
                                nums[one_idx] = 1
                                two_idx = i
                                nums[two_idx] = 2
                                zero_idx += 1
                                nums[zero_idx] = 0
                    elif nums[i] == 1:
                        if one_idx == -1:
                            if zero_idx == -1:
                                one_idx += 1
                                nums[one_idx] = 1
                                two_idx = i
                                nums[two_idx] = 2
                            else:
                                one_idx = zero_idx + 1
                                nums[one_idx] = 1
                                two_idx = i
                                nums[two_idx] = 2

                        else:
                            one_idx += 1
                            nums[one_idx] = 1
                            two_idx = i
                            nums[two_idx] = 2

            print("idx = ", i)
            print("nums = " , nums)
            print(zero_idx, one_idx, two_idx)
        return nums


a = Solution()
# a.sortColors([2,0,2,1,1,0])
a.sortColors([1,0])




class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        p, q = 0, 0
        k = len(nums) - 1

        while (q <= k):
            if p < q and nums[q] == 0:
                nums[p], nums[q] = nums[q], nums[p]
                p += 1
            elif nums[q] == 2:
                nums[k], nums[q] = nums[q], nums[k]
                k = k - 1
            else:
                q += 1
        return nums
