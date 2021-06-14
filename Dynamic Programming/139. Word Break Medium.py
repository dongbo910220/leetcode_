'''
https://leetcode.com/problems/word-break/
'''
#!/usr/bin/python
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        dict = {}
        for word in wordDict:
            dict[word]=1
        n = len(s)
        dp = [0] * (n+1)
        dp[0] = 1
        for i in range(1, n+1):
            for j in range(0, i):
                if s[j:i] in dict:
                    if dp[j] == 1:
                        dp[i] = 1
                        break
        return dp[n]

print(Solution().wordBreak("leetcode", ["leet", "code"]))

'''
Success
Details 
Runtime: 24 ms, faster than 83.68% of Python online submissions for Word Break.
Memory Usage: 12.8 MB, less than 6.38% of Python online submissions for Word Break.'''

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True
        for i in range(n):
            for j in range(i+1, n+1):
                if(dp[i] and (s[i:j] in wordDict)):
                    dp[j] = True
        return dp[-1]