class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        j = 0
        ans = False
        for idx, num in enumerate(nums):
            if num == val:
                ans = True
                continue
            else:
                nums[j] = num
                j += 1
        return j

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        n = len(nums)
        i = 0
        j = n - 1
        while i <= j:
            if nums[i] == val:
                # select right target
                while i <= j and nums[j] == val:
                    j -= 1
                if i <= j:
                    nums[i], nums[j] = nums[j], nums[i]
                    j -= 1
                    i += 1
                else:
                    break
            else:
                i += 1
        print(i)
        return i