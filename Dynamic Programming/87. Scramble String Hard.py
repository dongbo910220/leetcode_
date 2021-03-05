'''
https://leetcode.com/problems/scramble-string/
'''

class Solution(object):
    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        n = len(s1)
        if len(s1) != len(s2):
            return False
        if s1 == s2:
            return True
        if sorted(s1) != sorted(s2):
            return False
        f = self.isScramble
        for i in range(1,len(s1)):
            if (f(s1[i:], s2[i:]) and f(s1[:i], s2[:i])) or \
                (f(s1[:i], s2[(n-i):]) and f(s1[i:], s2[:(n-i)])):
                return True
        return False

'''
Success
Details 
Runtime: 32 ms, faster than 78.98% of Python online submissions for Scramble String.
Memory Usage: 12.9 MB, less than 50.00% of Python online submissions for Scramble String.
'''
