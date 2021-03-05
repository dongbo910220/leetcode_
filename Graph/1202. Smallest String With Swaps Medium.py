'''
https://leetcode.com/problems/smallest-string-with-swaps/
'''


class Solution(object):
    def smallestStringWithSwaps(self, s, pairs):
        """
        :type s: str
        :type pairs: List[List[int]]
        :rtype: str
        """
        graph = {}
        for node in range(len(s)):
            graph[node] = []
        for u ,v in pairs:
            graph[u].append(v)
            graph[v].append(u)


        position = {}
        for node in range(len(s)):
            if node not in position:
                idx = set()
                self.dfs(node, idx, graph)
                self.buildpos(s, idx, position)
        res = ''
        for i in range(len(s)):
            res += position[i]
        return res


    def buildpos(self, s, idx, position):
        idx_list = list(idx)
        char_list = []
        for idx in idx_list:
            char_list.append(s[idx])
        idx_list.sort()
        char_list.sort()
        for i in range(len(idx_list)):
            position[idx_list[i]] = char_list[i]


    def dfs(self, node, idx, graph):
        idx.add(node)
        for other in graph[node]:
            if other not in idx:
                self.dfs(other, idx, graph)

a = 'asdf'
print(a[2])

'''            
Success
Details 
Runtime: 1332 ms, faster than 23.77% of Python online submissions for Smallest String With Swaps.
Memory Usage: 75.8 MB, less than 100.00% of Python online submissions for Smallest String With Swaps.
'''

'''有问题  已经改好了'''


class Solution(object):
    def smallestStringWithSwaps(self, s, pairs):
        """
        :type s: str
        :type pairs: List[List[int]]
        :rtype: str
        """
        n = len(s)
        parents = [-1] * n
        idx_set = [[] for i in range(len(s))]

        for i, j in pairs:
            root1 = self.find(i, parents)
            root2 = self.find(j, parents)
            if root1 == root2:
                continue
            else:
                self.union(parents, root1, root2)

        for i in range(len(s)):
            root = self.find(i, parents)
            idx_set[root].append(i)

        #             if parents[parents[i]] <0:
        #                 idx_set[parents[i]].append(i)
        #             elif parents[i] < -1:
        #                 idx_set[i].append(i)

        position = {}
        for every_set in idx_set:
            if every_set:
                ss = []
                for i in every_set:
                    ss.append(s[i])
                ss.sort()
                every_set.sort()
                for i in range(len(every_set)):
                    position[every_set[i]] = ss[i]

        print(idx_set)
        print(parents)
        res = ''
        for i in range(len(s)):
            res += position[i]
        return res

    def union(self, S, root1, root2):
        if S[root2] < S[root1]:
            S[root2] += S[root1]
            S[root1] = root2
        else:
            S[root1] += S[root2]
            S[root2] = root1

    def find(self, i, parents):
        if parents[i] < 0:
            return i
        else:
            parents[i] = self.find(parents[i], parents)
            return parents[i]

'''
Success
Details 
Runtime: 1356 ms, faster than 21.31% of Python online submissions for Smallest String With Swaps.
Memory Usage: 55.9 MB, less than 100.00% of Python online submissions for Smallest String With Swaps.
'''



