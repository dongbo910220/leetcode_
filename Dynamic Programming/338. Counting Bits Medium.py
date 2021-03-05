'''
https://leetcode.com/problems/counting-bits/
'''

class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        dp = [0] * (num + 1)
        for i in range(1, nu m +1):
            dp[i] = dp[i >> 1] + (1 & i)

        return dp

'''
Success
Details 
Runtime: 68 ms, faster than 79.95% of Python online submissions for Counting Bits.
Memory Usage: 16.7 MB, less than 13.64% of Python online submissions for Counting Bits.
'''
