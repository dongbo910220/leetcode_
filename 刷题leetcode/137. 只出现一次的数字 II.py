class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        # print(sum())
        for i in range(32):
            total = sum((num >> i) & 1 for num in nums)
            if total % 3:
                if i == 31:
                    ans -= (1 << i)
                else:
                    ans += (1 << i)
        return ans