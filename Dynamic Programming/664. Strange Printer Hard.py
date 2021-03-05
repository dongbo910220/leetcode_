'''
https://leetcode.com/problems/strange-printer/

Success
Details
Runtime: 692 ms, faster than 44.62% of Python online submissions for Strange Printer.
Memory Usage: 13.8 MB, less than 70.77% of Python online submissions for Strange Printer.
'''


class Solution(object):
    def strangePrinter(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = len(s)
        self.table = [[0] * l for _ in range(l)]
        return self.turns(s, 0, l - 1)

    def turns(self, s, i, j):
        if i > j: return 0
        if self.table[i][j] > 0: return self.table[i][j]

        ans = self.turns(s, i, j - 1) + 1

        for k in range(i, j):
            if s[k] == s[j]:
                ans = min(ans, self.turns(s, i, k) + self.turns(s, k + 1, j - 1)) \
 \
                        self.table[i][j] = ans
        return ans