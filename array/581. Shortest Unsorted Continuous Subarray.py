'''
Given an integer array, you need to find one continuous subarray that if you only sort this subarray in ascending order, then the whole array will be sorted in ascending order, too.

You need to find the shortest such subarray and output its length.

Example 1:
Input: [2, 6, 4, 8, 10, 9, 15]
Output: 5
Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.
'''

# class Solution(object):
#     def findUnsortedSubarray(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         start = -1
#         end = -1
#         current_idx = -1
#         for i , num in enumerate(nums):
#             if(i == 0):
#                 last_num = num
#                 last_i = i
#             else:
#                 if (num < last_num):
#                     if(start == -1):
#                         start = last_i
#                         end = i
#                     else:
#                         end = i
#                 else:   # num >= last_num
#                     if num > last_num:
#                         last_num = num
#                         last_i = i
#         if end == start:
#             ans = 0
#         else:
#             ans = end - start + 1
#         return ans

# a = Solution()
# ans = a.findUnsortedSubarray([1, 2, 4, 5, 3])
# ans = a.findUnsortedSubarray([2, 6, 4, 8, 10, 9, 15])
# print(ans)

class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sNums = sorted(nums)
        start = end = 0

        for i in range(len(nums)):
            if sNums[i] != nums[i]:
                start = i
                break

        for i in range(len(nums)-1, 0, -1):
            if sNums[i] != nums[i]:
                end = i
                break
        return end - start + 1 if end - start else 0



# nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
# for i in range(len(nums)-1, -1, -1):
#     print(nums[i])