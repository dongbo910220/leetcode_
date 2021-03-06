A = [[1, 2, 3, 1], [1, 2 ,6, 2]]
print(max([max(row) for row in A]))

'''
https://leetcode.com/problems/maximum-length-of-repeated-subarray/submissions/
'''


class Solution(object):
    def findLength(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        dp = [[0 for _ in range(len(B) + 1)] for _ in range(len(A) + 1)]
        for i in range(1, len(A) + 1):
            for j in range(1, len(B) + 1):
                if A[i - 1] == B[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
        return max([max(row) for row in dp])
'''
Success
Details 
Runtime: 3248 ms, faster than 74.89% of Python online submissions for Maximum Length of Repeated Subarray.
Memory Usage: 34.5 MB, less than 45.11% of Python online submissions for Maximum Length of Repeated Subarray.
'''

