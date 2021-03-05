'''
https://leetcode.com/problems/house-robber/
'''
'''
Success
Details 
Runtime: 16 ms, faster than 82.25% of Python online submissions for House Robber.
Memory Usage: 12.8 MB, less than 6.38% of Python online submissions for House Robber.
'''

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        amount = [0] * (n + 2)
        for i in range(n):
            amount[i + 2] = max(amount[i + 1], nums[i] + amount[i])

        return amount[n + 1]

a = [1, 2, 3, 4, 5, 6]
print(a[1:])
print(a[:5])
print(a[5])