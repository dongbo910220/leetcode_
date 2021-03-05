'''
https://leetcode.com/problems/make-array-strictly-increasing/

'''

class Solution(object):
    def makeArrayIncreasing(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: int
        """
        dp = {-1:0}
        arr2.sort()
        for i in arr1:
            tmp = collections.defaultdict(lambda: float('inf'))
            for key in dp:
                if i > key:
                    tmp[i] = min(tmp[i], dp[key])
                loc = bisect.bisect_right(arr2, key)
                if loc < len(arr2):
                    tmp[arr2[loc]] = min(tmp[arr2[loc]], dp[key] + 1)
            dp = tmp
        if dp:
            return min(dp.values())
        return -1

'''
Success
Details 
Runtime: 748 ms, faster than 38.89% of Python online submissions for Make Array Strictly Increasing.
Memory Usage: 13 MB, less than 100.00% of Python online submissions for Make Array Strictly Increasing.
'''