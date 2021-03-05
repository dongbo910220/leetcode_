'''
https://leetcode.com/problems/n-queens/submissions/
'''


class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
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

        result = [[] for i in range(len(ans))]
        for i in range(len(ans)):
            for col in ans[i]:
                tmp = '.' * n
                result[i].append(tmp[:col] + 'Q' + tmp[col + 1:])
        return result

'''

Success
Details 
Runtime: 116 ms, faster than 31.83% of Python online submissions for N-Queens.
Memory Usage: 13 MB, less than 22.29% of Python online submissions for N-Queens.
'''