'''
https://leetcode.com/problems/evaluate-division/
'''
import collections

# class Solution(object):
#     def calcEquation(self, equations, values, queries):
#         """
#         :type equations: List[List[str]]
#         :type values: List[float]
#         :type queries: List[List[str]]
#         :rtype: List[float]
#         """
#         G = collections.defaultdict(dict)
#         for (x, y), v in zip(equations, values):
#             G[x][y] = v
#             G[y][x] = 1 / v
#
#         def bfs(src, dst):
#             if not (src in G and dst in G):
#                 return -1.0
#             q, seen = [(src, 1.0)], set()
#             for x, v in q:
#                 seen.add(x)
#                 if x == dst:
#                     return v
#                 for y in G[x]:
#                     if y not in seen:
#                         q.append((y, v * G[x][y]))
#             return -1.0
#         print(G)
#         return [bfs(s, d) for s, d in queries]
#
# # a = Solution()
# # print(a.calcEquation([["a","b"],["b","c"]],
# # [2.0,3.0],
# # [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]))
#
# # print(list(6))
# '''
# union find
# 另一个解释需要再看看
# https://leetcode.com/problems/evaluate-division/discuss/270993/Python-BFS-and-UF(detailed-explanation)
# '''
#
# class Solution(object):
#     def calcEquation(self, equations, values, queries):
#         """
#         :type equations: List[List[str]]
#         :type values: List[float]
#         :type queries: List[List[str]]
#         :rtype: List[float]
#         """
#         parents = {}
#         ratio = {}
#
#         def find(x):  # path compression
#             if parents[x] != x:
#                 ratio[x] *= ratio[parents[x]]
#                 parents[x] = find(parents[x])
#             return parents[x]
#
#         def union(x, y, k):
#             rx = find(x)
#             ry = find(y)
#             if rx != ry:
#                 parents[rx] = ry
#                 ratio[rx] = k * (ratio[y] / ratio[x])
#
#         for (A, B), k in zip(equations, values):
#             if A not in parents and B not in parents:
#                 parents[A] = B
#                 parents[B] = B
#                 ratio[A] = k
#                 ratio[B] = 1.0
#             elif A in parents and B in parents:
#                 union(A, B, k)
#             elif A in parents and B not in parents:
#                 ra = find(A)
#                 parents[B] = ra
#                 ratio[B] = 1 / k * ratio[A]
#             else:
#                 rb = find(B)
#                 parents[A] = rb
#                 ratio[A] = k * ratio[B]
#
#         res = []
#         for x, y in queries:
#             if x not in parents or y not in parents:
#                 res.append(-1.0)
#                 continue
#             rx = find(x)
#             ry = find(y)
#             if rx != ry:
#                 res.append(-1.0)
#             else:
#                 res.append(ratio[x] / ratio[y])
#
#         return res


class Solution1(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        parents = {}
        ratio = {}

        def find(x):
            if parents[x] != x:
                ratio[x] *= ratio[parents[x]]
                parents[x] = find(parents[x])
            return parents[x]

        def union(A, B, k):
            ra = find(A)
            rb = find(B)
            if ra != rb:
                parents[ra] = rb
                # ratio[A] = k * ratio[B]
                ratio[ra] = (1 / ratio[A]) * k * ratio[B]

        for (A, B), k in zip(equations, values):
            if A not in parents and B not in parents:
                parents[A] = B
                parents[B] = B
                ratio[A] = k
                ratio[B] = 1.0
            elif A in parents and B not in parents:
                ra = find(A)
                parents[B] = ra
                ratio[B] = 1 / k * ratio[A]
            elif A not in parents and B in parents:
                rb = find(B)
                parents[A] = rb
                ratio[A] = k * ratio[B]
            else:
                union(A, B, k)

        res = []
        print(ratio)
        for a, b in queries:
            if a not in parents or b not in parents:
                res.append(-1.0)
            else:
                ra = find(a)
                rb = find(b)
                if ra != rb:
                    res.append(-1.0)
                else:
                    ans = ratio[ra] / ratio[rb]
                    res.append(ans)
        return res

# a = Solution1()
#
# print(a.calcEquation([["a","b"],["b","c"]],
# [2.0,3.0],
# [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]))


class Solution2(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        ratio = {}
        parents = {}

        def find(A):
            if parents[A] != A:
                ratio[A] *= ratio[parents[A]]
                parents[A] = find(parents[A])
                # ratio[A] *= ratio[parents[A]]
            return parents[A]

        def union(A, B, v):
            ra = find(A)
            rb = find(B)
            if ra != rb:
                parents[ra] = rb
                ratio[ra] = v * ratio[B] / ratio[A]

        for (A, B), v in zip(equations, values):
            if A not in parents and B not in parents:
                parents[A] = B
                parents[B] = B
                ratio[A] = v
                ratio[B] = 1.0
            elif A not in parents and B in parents:
                rb = find(B)
                parents[A] = rb
                ratio[A] = v * ratio[B]
            elif A in parents and B not in parents:
                print("被调用了")
                ra = find(A)
                parents[B] = ra
                ratio[B] = 1 / v * ratio[A]
            else:  # A in parents and B  in parents:
                union(A, B, v)

        res = []
        print(parents)
        for A, B in queries:
            if A not in parents or B not in parents:
                res.append(-1.0)
            else:
                ra = find(A)
                rb = find(B)
                if ra != rb:
                    res.append(-1.0)
                else:
                    ans = ratio[A] / ratio[B]
                    res.append(ans)
        return res

a = Solution2()
#
# print(a.calcEquation([["a","b"],["b","c"]],
# [2.0,3.0],
# [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]))

# print(a.calcEquation([["a","b"],["e","f"],["b","e"]],
# [3.4,1.4,2.3],
# [["b","a"],["a","f"],["f","f"],["e","e"],["c","c"],["a","c"],["f","e"]]))

print(a.calcEquation([["a","b"],["b","c"],["c","d"]],
[3.0,4.0,5.0],
[["c","d"]]))