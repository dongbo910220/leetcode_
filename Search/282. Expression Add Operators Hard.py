'''
https://leetcode.com/problems/expression-add-operators/
'''


class Solution(object):
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        res = []
        self.target = target
        for i in range(1, len(num) + 1):
            if i == 1 or (i > 1 and num[0] != '0'):
                self.dfs(num[i:], num[:i], int(num[:i]), int(num[:i]), res)
        return res

    def dfs(self, num, temp, cur, prev, res):
        if not num:
            if cur == self.target:
                res.append(temp)
            return
        for i in range(1, len(num) + 1):
            val = num[:i]
            if i == 1 or (i > 1 and num[0] != '0'):
                self.dfs(num[i:], temp + '+' + val, cur + int(val), int(val), res)
                self.dfs(num[i:], temp + '-' + val, cur - int(val), -int(val), res)
                self.dfs(num[i:], temp + '*' + val, cur - prev + prev * int(val), prev * int(val), res)

'''
Success
Details 
Runtime: 2136 ms, faster than 8.25% of Python online submissions for Expression Add Operators.
Memory Usage: 13.4 MB, less than 6.16% of Python online submissions for Expression Add Operators.'''