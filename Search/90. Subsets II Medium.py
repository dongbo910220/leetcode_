'''
https://leetcode.com/problems/subsets-ii/
'''

class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = [[]]
        nums.sort()
        for i in range(len(nums)):
            if i == 0 or nums[i] != nums[i-1]:
                last = len(res)
            for j in range(len(res) - last, len(res)):
                res.append(res[j] + [nums[i]])
        return res

'''
Success
Details 
Runtime: 24 ms, faster than 77.39% of Python online submissions for Subsets II.
Memory Usage: 12.8 MB, less than 7.69% of Python online submissions for Subsets II.
'''