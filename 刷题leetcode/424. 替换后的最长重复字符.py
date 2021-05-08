class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        ret = i = 0
        count = collections.Counter()
        for j, c in enumerate(s):
            count[c] += 1
            while i < j and j - i + 1 - max(count.values()) > k:
                count[s[i]] -= 1
                i += 1
            ret = max(ret, j-i+1)
        return ret