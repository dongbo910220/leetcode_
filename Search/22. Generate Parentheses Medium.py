'''
https://leetcode.com/problems/generate-parentheses/

答案的可视化很好
https://leetcode.com/problems/generate-parentheses/discuss/10110/Simple-Python-DFS-solution-with-explanation
'''


class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if not n:
            return []
        left, right, ans = n, n, []
        self.dfs(left, right, ans, "")
        return ans

    def dfs(self, left, right, ans, String):
        if right < left:
            return
        if not left and not right:
            ans.append(String)
            return
        if left:
            self.dfs(left - 1, right, ans, String + "(")
        if right:
            self.dfs(left, right - 1, ans, String + ")")

print()

'''
Success
Details 
Runtime: 24 ms, faster than 63.58% of Python online submissions for Generate Parentheses.
Memory Usage: 12.7 MB, less than 5.88% of Python online submissions for Generate Parentheses.
'''