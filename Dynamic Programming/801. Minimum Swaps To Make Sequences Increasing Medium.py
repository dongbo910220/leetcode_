'''
https://leetcode.com/problems/minimum-swaps-to-make-sequences-increasing/
'''

class Solution(object):
    def minSwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        N = len(A)
        not_swap, swap = [N] * N, [N] * N
        not_swap[0], swap[0] = 0, 1
        for i in range(1, N):
            if A[i-1] < A[i] and B[i-1] < B[i]:
                swap[i] = swap[i-1] + 1
                not_swap[i] = not_swap[i-1]
            if A[i-1] < B[i] and B[i-1] < A[i]:
                swap[i] = min(swap[i], not_swap[i-1] + 1)
                not_swap[i] = min(not_swap[i], swap[i-1])
        return min(swap[-1], not_swap[-1])

'''
Success
Details 
Runtime: 92 ms, faster than 29.20% of Python online submissions for Minimum Swaps To Make Sequences Increasing.
Memory Usage: 13 MB, less than 8.33% of Python online submissions for Minimum Swaps To Make Sequences Increasing.
'''