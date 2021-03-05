'''
https://leetcode.com/problems/interleaving-string/
'''


class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        if len(s1) + len(s2) != len(s3):
            return False
        T = [[0] * (len(s2) + 1) for i in range(len(s1) + 1)]
        T[0][0] = 1

        for i in range(1, len(s1) + 1):
            if s1[i - 1] == s3[i - 1]:
                T[i][0] = T[i - 1][0]
            else:
                T[i][0] = 0

        for j in range(1, len(s2) + 1):
            if s2[j - 1] == s3[j - 1]:
                T[0][j] = T[0][j - 1]
            else:
                T[0][j] = 0

        for j in range(1, len(s2) + 1):
            for i in range(1, len(s1) + 1):
                if s3[i + j - 1] == s1[i - 1]:
                    T[i][j] = T[i - 1][j]
                    if T[i][j] == 1:
                        continue
                if s3[i + j - 1] == s2[j - 1]:
                    T[i][j] = T[i][j - 1]
                else:
                    T[i][j] = 0

        return bool(T[len(s1)][len(s2)])

'''
Success
Details 
Runtime: 36 ms, faster than 25.81% of Python online submissions for Interleaving String.
Memory Usage: 12.9 MB, less than 12.50% of Python online submissions for Interleaving String.'''