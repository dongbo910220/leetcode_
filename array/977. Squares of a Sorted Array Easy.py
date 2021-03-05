'''
https://leetcode.com/problems/squares-of-a-sorted-array/submissions/
'''
'''
Success
Details 
Runtime: 220 ms, faster than 33.32% of Python online submissions for Squares of a Sorted Array.
Memory Usage: 14.6 MB, less than 5.13% of Python online submissions for Squares of a Sorted Array.
'''

class Solution(object):
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        i = 0
        n = len(A)
        j = len(A) - 1
        res = []  # need to be reversed

        while i <= j:
            if abs(A[i]) > abs(A[j]):
                res.append(A[i] ** 2)
                print(A[i] ** 2)
                i += 1
            else:
                res.append(A[j] ** 2)
                j -= 1

        return res[::-1]