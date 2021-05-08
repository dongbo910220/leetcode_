class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        counter = collections.Counter(nums)
        h = []
        for key in counter:
            heappush(h, (-counter[key], key))

        res = []
        cnt = 0
        while cnt < k:
            freq, item = heappop(h)
            res.append(item)
            cnt += 1
        return res