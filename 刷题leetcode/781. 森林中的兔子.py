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


class Solution1(object):
    def numRabbits(self, answers):
        """
        :type answers: List[int]
        :rtype: int
        """
        nums = sorted(answers)
        print(nums)
        count = 0
        last = -1
        total = 0
        for num in nums:
            if num == last and count > 0:
                count -= 1
            else:
                count =  num
                total += (num + 1)
                last = num
        return count

print(Solution1().numRabbits([1, 1, 2]))