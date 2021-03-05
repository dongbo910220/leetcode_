'''
https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/
'''

class Solution(object):
    def shipWithinDays(self, weights, D):
        """
        :type weights: List[int]
        :type D: int
        :rtype: int
        """
        left, right= max(weights), sum(weights)
        while left < right:
            mid = (left + right) // 2
            cur = 0
            need = 1
            for w in weights:
                if cur + w > mid:
                    need += 1
                    cur = 0
                cur += w
            if need > D:
                left = mid + 1
            else:
                right = mid
        return left




'''
Success
Details
Runtime: 528 ms, faster than 42.94% of Python online submissions for Capacity To Ship Packages Within D Days.
Memory Usage: 15.2 MB, less than 11.88% of Python online submissions for Capacity To Ship Packages Within D Days.

'''