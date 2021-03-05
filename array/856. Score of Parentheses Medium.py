'''
https://leetcode.com/problems/score-of-parentheses/
'''

class Solution(object):
    def scoreOfParentheses(self, S):
        """
        :type S: str
        :rtype: int
        """
        cur = 0; stack = [];
        for c in S:
            if c == '(':
                stack.append(cur)
                cur = 0
            else:
                cur = cur + stack.pop() + max(cur, 1)
        return cur

'''
Success
Details 
Runtime: 12 ms, faster than 96.76% of Python online submissions for Score of Parentheses.
Memory Usage: 13 MB, less than 5.26% of Python online submissions for Score of Parentheses.
'''