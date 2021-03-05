'''
https://leetcode.com/problems/minimum-falling-path-sum/

Success
Details
Runtime: 104 ms, faster than 52.66% of Python online submissions for Minimum Falling Path Sum.
Memory Usage: 13.4 MB, less than 8.05% of Python online submissions for Minimum Falling Path Sum.
'''


class Solution(object):
    def minFallingPathSum(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        for i in range(1, len(A)):
            for j in range(len(A[0])):
                if j == 0:
                    A[i][j] = min(A[i][j] + A[i - 1][j], A[i][j] + A[i - 1][j + 1])
                elif j == len(A[0]) - 1:
                    A[i][j] = min(A[i][j] + A[i - 1][j], A[i][j] + A[i - 1][j - 1])
                else:
                    A[i][j] = min(A[i][j] + A[i - 1][j - 1], A[i][j] + A[i - 1][j], A[i][j] + A[i - 1][j + 1], )
        return min(A[len(A) - 1])
