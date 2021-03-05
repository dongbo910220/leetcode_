'''
https://leetcode.com/problems/longest-string-chain/
'''

class Solution(object):
    def longestStrChain(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        dp = {}
        for w in sorted(words, key=len):
            dp[w] = max(dp.get(w[:i] + w[i+1:],0) +1 for i in range(len(w)))
        # print(max(2, 5, 7))
        return max(dp.values())