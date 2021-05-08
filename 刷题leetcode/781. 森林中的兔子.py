class Solution(object):
    def numRabbits(self, answers):
        """
        :type answers: List[int]
        :rtype: int
        """
        nums = sorted(answers)
        i, ans, n = 0, 0, len(nums)
        while i < n:
            cur = nums[i]
            ans += (cur + 1)
            while cur > 0 and i + 1 < len(nums) and nums[i] == nums[i+1]:
                cur -= 1
                i += 1
            i += 1
        return ans