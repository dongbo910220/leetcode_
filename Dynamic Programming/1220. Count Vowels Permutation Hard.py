'''
https://leetcode.com/problems/count-vowels-permutation/
'''

class Solution(object):
    def countVowelPermutation(self, n):
        """
        :type n: int
        :rtype: int
        """
        a, e, i, o, u = 1, 1, 1, 1, 1
        for _ in range(n - 1):
            a, e, i, o, u = e + i + u, a + i, e + o, i, i + o
        return (a + e + i + o + u) % (10**9 + 7)

'''
Success
Details 
Runtime: 208 ms, faster than 71.88% of Python online submissions for Count Vowels Permutation.
Memory Usage: 13 MB, less than 46.88% of Python online submissions for Count Vowels Permutation.
'''