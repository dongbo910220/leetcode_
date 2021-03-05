'''
https://leetcode.com/problems/regions-cut-by-slashes/
'''

a = (1, 2)
print(a[1])
d  ={1:5, 2: 1}
print(d[min(d)])

d = [5, 6, 7, 8]
d.sort(reverse=True)
print(d)
# print([1 for dd in d if dd <= 7 ])
# print(sum(dd <= 7 for dd in d))



class Solution(object):
    def regionsBySlashes(self, grid):
        """
        :type grid: List[str]
        :rtype: int
        """
        f = {}

        def find(x):
            f.setdefault(x, x)
            if x != f[x]:  # path compression
                f[x] = find(f[x])
            return f[x]

        def union(x, y):
            f[find(x)] = find(y)

        for i in xrange(len(grid)):
            for j in range(len(grid)):
                if i:
                    union((i - 1, j, 2), (i, j, 0))
                if j:
                    union((i, j - 1, 1), (i, j, 3))
                if grid[i][j] != "/":
                    union((i, j, 0), (i, j, 1))
                    union((i, j, 2), (i, j, 3))
                if grid[i][j] != '\\':
                    union((i, j, 3), (i, j, 0))
                    union((i, j, 1), (i, j, 2))
        return len(set(map(find, f)))

'''
Success
Details 
Runtime: 324 ms, faster than 36.36% of Python online submissions for Regions Cut By Slashes.
Memory Usage: 17.3 MB, less than 50.00% of Python online submissions for Regions Cut By Slashes.
'''