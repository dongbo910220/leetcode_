class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        d = {}
        for w in strs:
            key = tuple(sorted(w))
            print(key)
            d[key] = d.get(key, []) + [w]
        return d.values()

a = '123'
print(sorted(a))
print(tuple(sorted(a)))