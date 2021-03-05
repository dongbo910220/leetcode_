class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        res = ""
        min_len = float('inf')
        for i in range(len(strs)):
            min_len = min(min_len, len(strs[i]))
        if not strs:
            return res
        for i in range(min_len):
            start = strs[0][i]
            has_commmon = True
            for j in range(len(strs)):
                if strs[j][i] != start:
                    has_commmon = False
                    break
            if has_commmon:
                res += start
            else:
                break
        return res

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        res = ""
        for tmp in zip(strs):
            tmp_set = set(tmp)
            if len(tmp_set) == 1:
                res += tmp[0]
            else:
                break
        return res

a = [1,2,3]
b = [4, 5, 6]
c = [4,5,6,7,8]
zipped = zip(a,b)
# print(*zipped)
# print(zip(a,c))
strs = ["flower","flow","flight"]
print(*strs)
res = ""
for tmp in zip(*strs):
    print(tmp)
    tmp_set = set(tmp)
    if len(tmp_set) == 1:
        res += tmp[0]
    else:
        break
print(res)



