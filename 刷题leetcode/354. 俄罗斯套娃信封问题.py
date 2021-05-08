class Solution(object):
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        nums = sorted(envelopes)
        # print(nums)
        dp =[1] * len(nums)
        def check(a, b):
            if a[0] > b[0] and a[1] > b[1]:
                return True
            else:
                return False

        for i in range(len(nums)):
            for j in range(i):
               if check(nums[i], nums[j]):
                   dp[i] = max(dp[i], dp[j]+1)
        return max(dp)


class Solution(object):
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        if not envelopes:
            return 0

        n = len(envelopes)
        envelopes.sort(key=lambda x: (x[0], -x[1]))

        h = []
        for i, e in enumerate(envelopes):
            j = bisect.bisect_left(h, e[1])
            if j < len(h):
                h[j] = e[1]
            else:
                h.append(e[1])
        return len(h)