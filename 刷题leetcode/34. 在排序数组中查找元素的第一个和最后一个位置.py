class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(nums)
        l = 0
        r = n - 1
        start = end = -1
        while l <= r:
            mid = (r - l) / 2 + l
            if nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid - 1
            else:
                #find the val
                start = end = mid
                while start >= 0 and nums[start] == target :
                    start -= 1
                if start < 0 or nums[start] != target:
                    start += 1
                while end <= n-1 and nums[end] == target:
                    end += 1
                if end > n-1 or nums[end] != target :
                    end -= 1
                break
        return [start, end]