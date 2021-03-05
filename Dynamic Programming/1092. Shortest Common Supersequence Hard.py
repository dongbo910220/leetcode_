'''
https://leetcode.com/problems/shortest-common-supersequence/
'''

class Solution(object):
    def shortestCommonSupersequence(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        def lcs(A, B):
            n, m = len(A), len(B)
            dp = [["" for _ in xrange( m +1)] for _ in xrange( n +1)]
            for i in xrange(n):
                for j in xrange(m):
                    if A[i] == B[j]:
                        dp[ i +1][ j +1] = dp[i][j] + A[i]
                    else:
                        dp[ i +1][ j +1] = max(dp[ i +1][j], dp[i][ j +1], key=len)
            return dp[-1][-1]

        res, i, j = "", 0, 0
        A = str1
        B = str2
        for c in lcs(str1, str2):
            while A[i] != c:
                res += A[i]
                i += 1
            while B[j] != c:
                res += B[j]
                j += 1
            res += c
            i += 1
            j += 1
        return res + A[i:] + B[j:]