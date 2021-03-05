'''
https://leetcode.com/problems/remove-invalid-parentheses/
'''


class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if not s:
            return ['']

        def check(s):
            l, r = 0, 0
            for ch in s:
                if ch == '(':
                    l += 1
                elif ch == ')':
                    if l > 0:
                        l -= 1
                    else:
                        r += 1
            return l, r

        def isLegal(s):
            l, r = 0, 0
            for i in range(len(s)):
                if s[i] == '(':
                    l += 1
                elif s[i] == ')':
                    if l > 0:
                        l -= 1
                    else:
                        return False
            if l == 0 and r == 0:
                return True
            else:
                return False

        def dfs(i, l, r, temp):
            if (i == len(s)) or (not l and not r):
                if isLegal(temp + s[i:]):
                    res.append(temp + s[i:])
                return

            if s[i] == ')':
                # remove it
                if r and (not temp or temp[-1] != ')'):
                    dfs(i + 1, l, r - 1, temp)
                # or not remove it
                dfs(i + 1, l, r, temp + s[i])

            elif s[i] == '(':
                if not r and l and (not temp or temp[-1] != '('):
                    dfs(i + 1, l - 1, r, temp)
                dfs(i + 1, l, r, temp + s[i])

            else:
                dfs(i + 1, l, r, temp + s[i])

        res = []
        l, r = check(s)
        dfs(0, l, r, '')
        return res if res else ['']

s = "abcasdf"
print(s[12:])

'''
Success
Details 
Runtime: 40 ms, faster than 90.31% of Python online submissions for Remove Invalid Parentheses.
Memory Usage: 12.7 MB, less than 31.58% of Python online submissions for Remove Invalid Parentheses.
'''