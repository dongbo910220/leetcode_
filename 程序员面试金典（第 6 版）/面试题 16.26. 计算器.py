class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        idx = 0
        s = s.replace(' ', '')
        print(s)
        while idx < len(s):
            operator = s[idx]
            if operator in "+-*/":
                idx += 1
            # print(c)
            # if c == ' ':
            #     idx += 1
            #     continue
            num = 0
            while idx < len(s) and s[idx] >= '0' and s[idx] <= '9':
                num = num * 10 + int(s[idx])
                idx += 1

            if operator == '+':
                pass
            elif operator == '-':
                num = -num
            elif operator == '*':
                num = stack.pop() * num
            elif operator == '/':
                num = stack.pop() // num
            else:
                pass #first num
            stack.append(num)
        total = 0
        while stack:
            total += stack.pop()
        return total

a = Solution()
print(a.calculate("14-3/2"))
