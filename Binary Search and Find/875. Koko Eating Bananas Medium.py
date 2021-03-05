'''
https://leetcode.com/problems/koko-eating-bananas/
'''


class Solution(object):
    def minEatingSpeed(self, piles, H):
        """
        :type piles: List[int]
        :type H: int
        :rtype: int
        """
        lo, hi = 1, max(piles)

        def canEat(k):
            time = 0
            for i in range(len(piles)):
                time += int(math.ceil(piles[i] / (float(k))))
                if time > H:
                    return False
            return True

        while lo < hi:

            mid = (lo + hi) // 2
            if canEat(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo


'''
Success
Details
Runtime: 1036 ms, faster than 5.17% of Python online submissions for Koko Eating Bananas.
Memory Usage: 13.7 MB, less than 58.16% of Python online submissions for Koko Eating Bananas.
'''