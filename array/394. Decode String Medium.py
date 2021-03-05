'''
https://leetcode.com/problems/decode-string/
'''

class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []; curNum = 0; curString = ''
        for c in s:
            if c == '[':
                stack.append(curString)
                stack.append(curNum)
                curString = ''
                curNum = 0
            elif c == ']':
                num = stack.pop()
                prevString = stack.pop()
                curString = prevString + num*curString
            elif c.isdigit():
                curNum = curNum * 10 + int(c)
            else:
                curString += c
        return curString

'''
Success
Details 
Runtime: 12 ms, faster than 94.45% of Python online submissions for Decode String.
Memory Usage: 12.6 MB, less than 5.88% of Python online submissions for Decode String.
'''