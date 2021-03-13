'''
执行结果：
通过
显示详情
执行用时：52 ms, 在所有 Python 提交中击败了95.22% 的用户
内存消耗：12.9 MB, 在所有 Python 提交中击败了70.66% 的用户
'''
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        translations = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        number = 0
        s = s.replace("IV", "IIII").replace("IX","VIIII")
        s = s.replace("XL", "XXXX").replace("XC", "LXXXX")
        s = s.replace("CD", "CCCC").replace("CM", "DCCCC")
        for char in s:
            number += translations[char]
        return number


class Solution1(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        h = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        num = 0
        prev = 0
        for c in s:
            if h[c] <= prev:
                num += h[c]
            else:
                num += h[c] - 2 * prev
            prev = h[c]
        return num

# print(Solution1().romanToInt("IV"))