'''
https://leetcode.com/problems/word-break-ii/
'''


class Solution(object):

    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        dict = {}
        for word in wordDict:
            dict[word] = 1
        res = []
        memo = {}
        res = self.helper(s, memo, dict)
        print(memo)
        return res

    def helper(self, s, memo, dict):
        if s in memo:
            return memo[s]
        if not s:
            return 1
        res = []
        for i in range(len(s)):
            if s[:i + 1] in dict:
                res_part = self.helper(s[i + 1:], memo, dict)
                if res_part == 1:
                    res.append(s[:i + 1])
                else:
                    for item in res_part:
                        item = s[:i + 1] + " " + item
                        res.append(item)
        memo[s[:i + 1]] = res
        return res

print(Solution().wordBreak("catsanddog", ["cat", "cats", "and", "sand", "dog"]))
'''
Success
Details 
Runtime: 24 ms, faster than 96.98% of Python online submissions for Word Break II.
Memory Usage: 13 MB, less than 7.69% of Python online submissions for Word Break II.'''