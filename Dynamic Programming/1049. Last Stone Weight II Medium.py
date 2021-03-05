'''
https://leetcode.com/problems/last-stone-weight-ii/
'''


class Solution(object):
    def lastStoneWeightII(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        total = sum(stones)
        target_ = total / 2.0
        target = int(target_)
        dp = [0] * (target + 1)
        for stone in stones:
            for i in range(target, stone - 1, -1):
                # print(i, i-stone)
                dp[i] = max(dp[i], dp[i - stone] + stone)
        return int((target_ - dp[target]) * 2)

'''
Success
Details 
Runtime: 36 ms, faster than 65.93% of Python online submissions for Last Stone Weight II.
Memory Usage: 12.8 MB, less than 66.67% of Python online submissions for Last Stone Weight II.'''
