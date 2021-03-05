'''
https://leetcode.com/problems/n-queens-ii/submissions/

Success
Details
Runtime: 88 ms, faster than 36.00% of Python online submissions for N-Queens II.
Memory Usage: 12.7 MB, less than 59.69% of Python online submissions for N-Queens II.
'''


class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans = []

        def dfs(nums, row):
            if row == n:
                print(nums)
                ans.append(nums[:])
                return
            for col in range(n):
                nums[row] = col
                if valid(nums, row):
                    dfs(nums, row + 1)

        def valid(nums, row):
            for i in range(row):
                if nums[i] == nums[row] or abs(nums[i] - nums[row]) == abs(row - i):
                    return False
            return True

        # initialize the matrix and row
        dfs([None for _ in range(n)], 0)
        print(ans)

        return len(ans)