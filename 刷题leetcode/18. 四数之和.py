class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        res = []
        n = len(nums)
        for i in range(len(nums)-3):
            #delete
            if (i != 0) and nums[i] == nums[i-1]:
                continue
            if nums[i] + nums[i+1] + nums[i+2] + nums[i+3] > target:
                break
            if nums[i] + nums[n-1] + nums[n-2] + nums[n-3] < target:
                continue
            for j in range(i+1, len(nums)-2):
                if j != i + 1 and nums[j-1] == nums[j]:
                    continue
                if nums[i] + nums[j] + nums[j+1] + nums[j+2] > target:
                    break
                if nums[i] + nums[j] + nums[n-1] + nums[n-2] < target:
                    continue
                l = j + 1
                r = len(nums) - 1
                while l < r:
                    if nums[i] + nums[j] + nums[l] + nums[r] == target:
                        res.append([nums[i],nums[j],nums[l], nums[r]])
                        while l+1 < r and nums[l+1] == nums[l]:
                            l = l+1
                        l = l+1
                        while l < r-1 and nums[r] == nums[r-1]:
                            r = r - 1
                        r = r - 1
                    elif nums[i] + nums[j] + nums[l] + nums[r] < target:
                        l += 1
                    elif nums[i] + nums[j] + nums[l] + nums[r] > target:
                        r -= 1
        return res

a = Solution()
print(a.fourSum([1,0,-1,0,-2,2], 0))