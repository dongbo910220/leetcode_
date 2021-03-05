'''
https://leetcode.com/problems/count-of-smaller-numbers-after-self/
'''


class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        rank, N, res = {val: i + 1 for i, val in enumerate(sorted(nums))}, len(nums), []
        BITree = [0] * (N + 1)

        def update(i):
            while i <= N:
                BITree[i] += 1
                i += (i & -i)

        def getSum(i):
            s = 0
            while i:
                s += BITree[i]
                i -= (i & -i)
            return s

        for x in reversed(nums):
            res += [getSum(rank[x] - 1)]  # minus self
            update(rank[x])
        return res[::-1]

'''
Success
Details 
Runtime: 104 ms, faster than 85.17% of Python online submissions for Count of Smaller Numbers After Self.
Memory Usage: 15.4 MB, less than 37.50% of Python online submissions for Count of Smaller Numbers After Self.
'''