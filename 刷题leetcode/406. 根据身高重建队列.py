'''
执行结果：
通过
显示详情
执行用时：24 ms, 在所有 Python 提交中击败了98.01% 的用户
内存消耗：13.5 MB, 在所有 Python 提交中击败了75.34% 的用户
'''


class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        people_dict = {}
        for p in people:
            h, k = p[0], p[1]
            # set default value if not exist else do nothing
            people_dict.setdefault(h, [])
            people_dict[h].append(k)

        result = []

        for h in sorted(people_dict.keys(), reverse=True):
            people_dict[h].sort()
            for k in people_dict[h]:
                result.insert(k, [h, k])

        return result