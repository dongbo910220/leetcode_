class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        mapping = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
                   '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        res = []
        if len(digits) == 0:
            return res
        self.dfs(res, mapping, 0, digits, "")
        return res

    def dfs(self, res, mapping, idx, digits, path):
        if len(path) == len(digits):
            res.append(path)
            return
        else:
            for c in mapping[digits[idx]]:
                self.dfs(res, mapping, idx+1, digits,path+c)


'''
Success
Details 
Runtime: 12 ms, faster than 97.42% of Python online submissions for Letter Combinations of a Phone Number.
Memory Usage: 12.9 MB, less than 7.14% of Python online submissions for Letter Combinations of a Phone Number.
'''


class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        interpret_digit = {
            '1': '',
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
            '0': ' '
        }

        all_combination = [''] if digits else []
        for digit in digits:
            cur = []
            for letter in interpret_digit[digit]:
                for combination in all_combination:
                    cur.append(combination + letter)
            all_combination = cur
        return all_combination

