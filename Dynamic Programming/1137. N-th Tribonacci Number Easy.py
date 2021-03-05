'''
https://leetcode.com/problems/n-th-tribonacci-number/

Success
Details
Runtime: 24 ms, faster than 13.17% of Python online submissions for N-th Tribonacci Number.
Memory Usage: 12.8 MB, less than 24.64% of Python online submissions for N-th Tribonacci Number.
'''



class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        len_n = n
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1

        T = [0] * (n + 1)
        T[1] = 1
        T[2] = 1
        for i in range(3, n + 1):
            T[i] = T[i - 3] + T[i - 2] + T[i - 1]
        return T[n]