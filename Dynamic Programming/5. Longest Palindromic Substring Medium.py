'''
https://leetcode.com/problems/longest-palindromic-substring/
'''


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        palindrome = ""
        for i in range(len(s)):
            #基数情况
            p1 = self.palindromic(s, i, i)
            if len(p1) > len(palindrome):
                palindrome = p1
            # 偶数情况
            p2 = self.palindromic(s, i, i + 1)
            if len(p2) > len(palindrome):
                palindrome = p2

        return palindrome

    def palindromic(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l + 1:r]

'''    
Success
Details 
Runtime: 756 ms, faster than 88.02% of Python online submissions for Longest Palindromic Substring.
Memory Usage: 12.7 MB, less than 39.73% of Python online submissions for Longest Palindromic Substring.
'''