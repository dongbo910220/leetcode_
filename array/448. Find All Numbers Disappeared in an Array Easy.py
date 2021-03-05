'''
Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements of [1, n] inclusive that do not appear in this array.

Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.

Example:

Input:
[4,3,2,7,8,2,3,1]

Output:
[5,6]

'''

class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        u  = range(1, len(nums) + 1)
        l = set(sorted(nums))
        if len(l) > 0:
            return list(set(u) - l)
        else:
            return []

class Solution_2(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        for n in nums:
            a = abs(n) - 1
            if nums[a] > 0: nums[a] *= -1
            print(a, nums[a])
        return [i + 1 for i in range(len(nums)) if nums[i] > 0]




a = Solution_2()
print(a.findDisappearedNumbers([4,3,2,7,8,2,3,1]))

a = set([1, 2, 3, 4, 5])
b = set([1, 2, 3, 3, 5])
print(list(a - b))










