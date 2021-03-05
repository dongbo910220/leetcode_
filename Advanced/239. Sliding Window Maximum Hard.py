'''
https://leetcode.com/problems/sliding-window-maximum/
'''


class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if not nums:
            return []
        if k == 0 or k == 1:
            return nums

        queue = collections.deque()
        result = []

        for i in range(k):
            while queue and nums[queue[-1]] < nums[i]:
                queue.pop()
            queue.append(i)

        for i in range(k, len(nums)):
            result.append(nums[queue[0]])
            if queue[0] < i - k + 1:
                queue.popleft()
            while queue and nums[queue[-1]] < nums[i]:
                queue.pop()
            queue.append(i)
        result.append(nums[queue[0]])
        return result







'''
Success
Details 
Runtime: 288 ms, faster than 80.13% of Python online submissions for Sliding Window Maximum.
Memory Usage: 23.3 MB, less than 47.71% of Python online submissions for Sliding Window Maximum.
'''