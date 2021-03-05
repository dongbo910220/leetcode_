'''
https://leetcode.com/problems/k-th-smallest-prime-fraction/

'''

import bisect
class Solution(object):
    def kthSmallestPrimeFraction(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: List[int]
        """
        l, r, N = 0.0, 1.0, len(A)
        while True:
            m = (l + r) / 2
            border = [bisect.bisect(A, A[i] / m) for i in xrange(N)]

            cur = sum(N - i for i in border)  # smaller than m
            if cur > K:
                r = m
            elif cur < K:
                l = m
            else:
                return max([(A[i], A[j]) for i, j in enumerate(border) if j < N], key=lambda x: float(x[0]) / x[1])

'''
Success
Details 
Runtime: 228 ms, faster than 77.27% of Python online submissions for K-th Smallest Prime Fraction.
Memory Usage: 13.3 MB, less than 25.00% of Python online submissions for K-th Smallest Prime Fraction.
'''



















import bisect
a = [ 3 ,4, 6 ,10]
for idx, val in enumerate(a):
    print(idx, val)


print(bisect.bisect(a, 0.5))