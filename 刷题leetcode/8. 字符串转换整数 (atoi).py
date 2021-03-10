# s = ' 123asdf '
# print(s.strip())
# print(list(s.strip()))

class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0
        ls = list(s.strip())

        if len(ls) == 0:
            return 0
        sign = -1 if ls[0] == '-' else 1
        if ls[0] in ['+', '-']: del ls[0]
        ret, i  = 0, 0
        while i < len(ls) and ls[i].isdigit():
            ret = ret * 10 + ord(ls[i]) - ord('0')
            i += 1
        if sign == -1:
            ret = max(- 2 **31, sign * ret)
        else:
            ret = min(2 **31 -1, ret)
        return ret