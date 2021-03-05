'''
https://leetcode.com/problems/different-ways-to-add-parentheses/submissions/
'''



class Solution(object):
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        if input.isdigit():
            return [int(input)]
        res = []
        for i in range(len(input)):
            if input[i] in "+-*":
                res_set1 = self.diffWaysToCompute(input[:i])
                res_set2 = self.diffWaysToCompute(input[i + 1:])
                for res1 in res_set1:
                    for res2 in res_set2:
                        res.append(self.helper(res1, res2, input[i]))
        return res

    def helper(self, res1, res2, op):
        if op == '+':
            return res1 + res2
        if op == '-':
            return res1 - res2
        if op == '*':
            return res1 * res2

'''
Success
Details 
Runtime: 20 ms, faster than 87.77% of Python online submissions for Different Ways to Add Parentheses.
Memory Usage: 12.9 MB, less than 23.38% of Python online submissions for Different Ways to Add Parentheses.
'''