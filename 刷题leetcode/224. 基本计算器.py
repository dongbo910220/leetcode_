'''
https://leetcode-cn.com/problems/basic-calculator/solution/ru-he-xiang-dao-yong-zhan-si-lu-lai-zi-y-gpca/
'''
#不用动脑子版本
class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        res, num, sign = 0, 0, 1
        stack = []
        for c in s:
            if c.isdigit():
                num = num * 10 + int(c)
            elif c in "+-":
                res += sign * num
                if c == "-":
                    sign = -1
                else:
                    sign = 1
                num = 0
            elif c == "(":
                stack.append(res)
                stack.append(sign)
                res = 0
                num = 0
                sign = 1
            elif c == ")":
                res += sign * num
                res *= stack.pop()
                res += stack.pop()
                num = 0
                sign = 1
        res += sign * num
        return res


class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        res, num, sign = 0, 0, 1
        stack = []
        for c in s:
            if c.isdigit():
                num = num * 10 + int(c)
            elif c in "+-":
                res += sign * num
                # update the num
                num = 0
                sign = 1 if c == "+" else -1
            elif c == '(':
                # using stack to keep previous status
                stack.append(res)
                stack.append(sign)
                res = 0
                sign = 1
            elif c == ')':
                res += sign * num
                num = 0
                sign = 1
                res = stack.pop() * res
                res += stack.pop()

        # after the for loop:
        res += sign * num
        return res

class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        res, num, sign = 0, 0, 1
        stack = []
        for c in s:
            if c.isdigit():
                num = 10 * num + int(c)
            elif c in "+-":
                res += sign * num
                num = 0
                sign = 1 if c == '+' else -1
            elif c == '(':
                stack.append(res)
                stack.append(sign)
                res = 0
                sign = 1
            elif c == ')':
                res += sign * num
                num = 0
                res *= stack.pop()
                res += stack.pop()
        res += sign * num
        return res