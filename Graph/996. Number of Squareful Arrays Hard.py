'''
https://leetcode.com/problems/number-of-squareful-arrays/
'''

from collections import Counter

import collections
class Solution(object):
    def numSquarefulPerms(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        c = collections.Counter(A)
        candiates = {i: {j for j in c if int((i + j) ** 0.5) ** 2 == (i + j)} for i in c}

        def dfs(x, left=len(A) - 1):
            c[x] -= 1
            count = sum(dfs(y, left - 1) for y in candiates[x] if c[y]) if left else 1
            c[x] += 1
            return count

        return sum(map(dfs, c))

'''
Success
Details 
Runtime: 16 ms, faster than 89.53% of Python online submissions for Number of Squareful Arrays.
Memory Usage: 12.9 MB, less than 50.00% of Python online submissions for Number of Squareful Arrays.
'''