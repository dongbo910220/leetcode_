stack = ['']
stack.append('')
print(len(stack))
s = "asdf"
s + '2'
print(s)
print(s)


class Solution(object):
    def reverseParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = ['']
        for c in s:
            if c == '(':
                stack.append('')
            elif c == ')':
                rev = stack.pop()
                rev = rev[::-1]
                stack[-1] = stack[-1] + rev
            else:
                # c is char
                stack[-1] = stack[-1] + c
        return stack.pop()
