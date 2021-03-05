'''
https://leetcode.com/problems/partition-array-for-maximum-sum/
'''

class Solution(object):
    def maxSumAfterPartitioning(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        N = len(A)
        dp = [0] * (N + 1)
        for i in range(N + 1):
            j = i - 1
            maxval = dp[i]
            while i - j <= K and j >= 0:
                maxval = max(maxval, A[j])
                dp[i] = max(dp[i], dp[j] + (i - j) * maxval)
                j -= 1
        print(dp)
        return dp[N]

'''
Success
Details 
Runtime: 392 ms, faster than 83.72% of Python online submissions for Partition Array for Maximum Sum.
Memory Usage: 13 MB, less than 20.15% of Python online submissions for Partition Array for Maximum Sum.'''