'''
Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.

Example 1:

Input: [3,2,3]
Output: 3
Example 2:

Input: [2,2,1,1,1,2,2]
Output: 2
'''
import collections

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        h = {}
        for i, num in enumerate(nums):
            if num in h.keys():
                h[num] = h[num] + 1
            else:
                h[num] = 1
        max_num = max(h, key=h.get)
        # print(h.keys())
        return max_num

class Solution_Collections(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counts = collections.Counter(nums)
        return max(counts.keys(), key=counts.get)


class Solution_OneLine(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sorted(nums)[len(nums)/2]


a = Solution()
ans = a.majorityElement([2,2,1,1,1,2,2])
print(ans)