'''
Your are given an array of positive integers nums.

Count and print the number of (contiguous) subarrays where the product of all the elements in the subarray is less than k.

Example 1:
Input: nums = [10, 5, 2, 6], k = 100
Output: 8
Explanation: The 8 subarrays that have product less than 100 are: [10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6].
Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.
Note:

0 < nums.length <= 50000.
0 < nums[i] < 1000.
0 <= k < 10^6.

'''

#超时哈哈
class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        sum = 1
        n = len(nums)
        product_sum = [0] * n  # not sure
        res = 0
        for i in range(len(nums)):
            sum *= nums[i]
            product_sum[i] = sum
        for i in range(len(nums)):
            if product_sum[i] < k:
                print(i)
                res += 1
            for j in range(0, i):
                # print('i', i)
                # print('j', j)
                if product_sum[i] // product_sum[j] < k:
                    # print(j,i)
                    res += 1
                else:
                    pass
        return res

# a = Solution()
# print(a.numSubarrayProductLessThanK([10,9,10,4,3,8,3,3,6,2,10,10,9,3] ,19))

# for i in range(0, 5):
#     for j in range(0, i):
#         # print('i', i)
#         print('j', j)

class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        sum = 1
        n = len(nums)
        res = 0
        left = 0
        for right in range(n):
            sum *= nums[right]
            while(left <= right and sum >= k):
                sum //= nums[left]
                left += 1
            res += right -left + 1
        return res

print(5 / 2)

