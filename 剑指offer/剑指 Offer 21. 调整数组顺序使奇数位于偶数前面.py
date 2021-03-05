class Solution(object):
    def exchange(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        m = len(nums)
        j = m - 1
        i = 0
        def isOdd(num):
            if num % 2 == 1:
                return True
            else:
                return False

        while i < j:
            if not isOdd(nums[i]):  #nums[i] is even
                while i < j:
                    if isOdd(nums[j]):
                        break
                    else:
                        j -= 1
                if i != j:
                    tmp = nums[i]
                    nums[i] = nums[j]
                    nums[j] = tmp
                else:
                    break
            i += 1
        return nums