class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        strs = map(str, nums)
        def compare(x, y): return int(y+x) - int(x+y)
        nums = sorted(strs, cmp=compare)
        ans = ''
        for num in nums:
            ans += num
        return ans if int(ans) != 0 else '0'


        # strs = map(str, nums)
        # print(strs)
        # def compare(x, y):
        #     return - ((int(x + y) - int(y + x))
        # # strs = map(str, nums)
        # nums = sorted(strs, cmp=compare)
        # ans = ''
        # for s in nums:
        #     ans += s
        # return ans