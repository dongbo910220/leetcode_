'''
https://leetcode.com/problems/next-greater-element-ii/
'''

class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        A = nums
        stack, res = [], [-1] * len(A)
        for i in range(len(A)) * 2:
            # print(i)
            while stack and (A[stack[-1]] < A[i]):
                res[stack.pop()] = A[i]
            stack.append(i)
        return res

'''
Success
Details 
Runtime: 320 ms, faster than 20.59% of Python online submissions for Next Greater Element II.
Memory Usage: 14.4 MB, less than 66.26% of Python online submissions for Next Greater Element II.'''