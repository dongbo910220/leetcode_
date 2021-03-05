'''
https://leetcode.com/problems/next-greater-element-i/
'''

class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        h = {}
        stack = []
        res = [-1] * len(nums2)
        for i in range(len(nums2)):
            while stack and nums2[stack[-1]] < nums2[i]:
                res[stack.pop()] = nums2[i]
            stack.append(i)
        for idx, val in enumerate(res):
            h[nums2[idx]] = val
        ans = [0] * len(nums1)
        for i in range(len(nums1)):
            ans[i] = h[nums1[i]]
        return ans

'''
Success
Details 
Runtime: 44 ms, faster than 52.14% of Python online submissions for Next Greater Element I.
Memory Usage: 12.9 MB, less than 82.48% of Python online submissions for Next Greater Element I.
'''