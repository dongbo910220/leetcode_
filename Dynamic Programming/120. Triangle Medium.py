'''
https://leetcode.com/problems/triangle/
'''


class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        n = len(triangle)
        if n == 0:
            return 0
        dp = triangle[n - 1]
        num = n - 1
        while num > 0:  # ?
            for i in range(num):
                dp[i] = min(dp[i], dp[i + 1]) + triangle[num - 1][i]
            num -= 1

        return dp[0]


'''
Success
Details 
Runtime: 40 ms, faster than 92.81% of Python online submissions for Triangle.
Memory Usage: 13.1 MB, less than 16.67% of Python online submissions for Triangle.
'''
# for i in range(5, -1 , -1):
#     print(i)