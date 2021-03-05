'''
https://leetcode.com/problems/longest-arithmetic-subsequence-of-given-difference/


'''

class Solution(object):
    def longestSubsequence(self, arr, difference):
        """
        :type arr: List[int]
        :type difference: int
        :rtype: int
        """
        res = {}
        for num in arr:
            res[num] = res[num - difference] + 1 if num - difference in res else 1
        return max(res.values())

'''
Success
Details 
Runtime: 588 ms, faster than 43.81% of Python online submissions for Longest Arithmetic Subsequence of Given Difference.
Memory Usage: 23.9 MB, less than 53.06% of Python online submissions for Longest Arithmetic Subsequence of Given Difference.'''