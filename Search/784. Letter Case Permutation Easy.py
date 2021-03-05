'''
https://leetcode.com/problems/letter-case-permutation/
'''

class Solution(object):
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        res = ['']
        for ch in S:
            if ch.isalpha():
                res = [i+j for i in res for j in [ch.upper(), ch.lower()]]
            else:
                res = [i + ch for i in res]
        return res

'''
Success
Details 
Runtime: 40 ms, faster than 91.77% of Python online submissions for Letter Case Permutation.
Memory Usage: 13.6 MB, less than 20.00% of Python online submissions for Letter Case Permutation.
'''