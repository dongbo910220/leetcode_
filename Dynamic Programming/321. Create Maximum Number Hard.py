'''
https://leetcode.com/problems/create-maximum-number/
'''


class Solution(object):
    def maxNumber(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[int]
        """
        maxval = 0
        maxList = []
        for i in range(k + 1):
            j = k - i
            if i > len(nums1) or j > len(nums2):
                continue
            list1 = self.getMax(nums1, i)
            list2 = self.getMax(nums2, k - i)
            m1 = self.merge(list2, list1)
            # print("list1", list1)
            # print("list2", list2)
            # print("m1", m1)
            if m1 > maxList:
                # maxval = sum(m1)
                maxList = m1
        return maxList

    def getMax(self, nums, k):
        res = []
        rest = len(nums) - k
        if k == 0:
            return res
        for num in nums:
            if not res:
                res.append(num)
            else:
                while res != [] and num > res[-1] and rest > 0:
                    rest -= 1
                    res.pop()
                res.append(num)
        return res[:k]

    def merge(self, nums1, nums2):
        ans = []
        while nums1 or nums2:
            if nums1 > nums2:
                ans.append(nums1[0])
                nums1 = nums1[1:]
            else:
                ans.append(nums2[0])
                nums2 = nums2[1:]
        return ans

'''
Success
Details 
Runtime: 656 ms, faster than 32.04% of Python online submissions for Create Maximum Number.
Memory Usage: 12.7 MB, less than 50.00% of Python online submissions for Create Maximum Number.
'''