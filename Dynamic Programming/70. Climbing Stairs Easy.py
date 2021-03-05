'''
https://leetcode.com/problems/climbing-stairs/
'''
'''
Success
Details 
Runtime: 12 ms, faster than 88.74% of Python online submissions for Climbing Stairs.
Memory Usage: 12.7 MB, less than 6.25% of Python online submissions for Climbing Stairs.
'''


class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        if n == 2:
            return 2

        list = [0] * n
        list[0] = 1
        list[1] = 2
        for i in range(2, n):
            list[i] = list[i - 1] + list[i - 2]
        return list[n - 1]

girl_str = "love You"

for everyChar in girl_str:

    print (everyChar)