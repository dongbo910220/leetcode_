'''
https://leetcode.com/problems/greatest-sum-divisible-by-three/
'''


class Solution(object):
    def maxSumDivThree(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        N = len(nums)
        dp = [[0] * 3 for _ in range(N + 1)]
        dp[0][1] = dp[0][2] = float('-inf')
        for idx, num in enumerate(nums):
            i = idx + 1
            if num % 3 == 0:
                print(num, 0)
                dp[i][0] = max(dp[i - 1][0], dp[i - 1][0] + num)
                dp[i][1] = max(dp[i - 1][1], dp[i - 1][1] + num)
                dp[i][2] = max(dp[i - 1][2], dp[i - 1][2] + num)

            elif num % 3 == 1:
                print(num, 1)
                dp[i][0] = max(dp[i - 1][0], dp[i - 1][2] + num)
                dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] + num)
                dp[i][2] = max(dp[i - 1][2], dp[i - 1][1] + num)

            else:
                # num % 3 == 2:
                print(num, 2)
                dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + num)
                dp[i][1] = max(dp[i - 1][1], dp[i - 1][2] + num)
                dp[i][2] = max(dp[i - 1][2], dp[i - 1][0] + num)

        # print(dp)
        return dp[N][0]

'''
Success
Details 
Runtime: 608 ms, faster than 16.26% of Python online submissions for Greatest Sum Divisible by Three.
Memory Usage: 21.8 MB, less than 11.82% of Python online submissions for Greatest Sum Divisible by Three.
'''