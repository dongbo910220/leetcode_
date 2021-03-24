class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not haystack and not needle:
            return 0
        if not haystack:
            return -1
        if not needle:
            return 0
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i] == needle[0]:
                isFind = True
                for j in range(1, len(needle)):
                    if haystack[i + j] != needle[j]:
                        isFind = False
                        break
                if isFind:
                    return i
        return -1