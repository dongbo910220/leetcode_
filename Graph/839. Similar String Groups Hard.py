'''
https://leetcode.com/problems/similar-string-groups/
'''
'''
Success
Details 
Runtime: 8992 ms, faster than 66.05% of Python online submissions for Similar String Groups.
Memory Usage: 13.9 MB, less than 100.00% of Python online submissions for Similar String Groups.
'''

# print(list(range(5)))
class Solution(object):
    def numSimilarGroups(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        A = list(set(A))
        n = len(A)
        if n <= 1:
            return n
        wordlen = len(A[0])

        def similar(word1, word2):
            diff = i = 0
            while i < wordlen and diff <= 2:
                if word1[i] != word2[i]:
                    diff += 1
                i += 1
            return diff <= 2

        parents = list(range(n))

        def find(a):  # path compression
            if parents[a] != a:
                parents[a] = find(parents[a])
            return parents[a]

        def union(a, b):
            ra = find(a)
            rb = find(b)
            parents[ra] = rb

        for i in range(n):
            for j in range(i + 1, n):
                if similar(A[i], A[j]):
                    union(i, j)

        return sum([1 for i, e in enumerate(parents) if i == e])

'''
换成xrange快很多
'''
class Solution(object):
    def numSimilarGroups(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        A = list(set(A))
        n = len(A)
        if n <= 1:
            return n
        wordlen = len(A[0])

        def similar(word1, word2):
            diff = i = 0
            while i < wordlen and diff <= 2:
                if word1[i] != word2[i]:
                    diff += 1
                i += 1
            return diff <= 2

        parents = list(xrange(n))

        def find(a):  # path compression
            if parents[a] != a:
                parents[a] = find(parents[a])
            return parents[a]

        def union(a, b):
            parents[find(a)] = find(b)

        for i in xrange(n):
            for j in xrange(i + 1, n):
                if similar(A[i], A[j]):
                    union(i, j)

        return sum([1 for i, e in enumerate(parents) if i == e])