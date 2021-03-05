'''
https://leetcode.com/problems/largest-component-size-by-common-factor/
'''
A = [2, 3, 8]
idx_lookup = {A[i]: i for i in range(len(A))}
print(idx_lookup)
'''
Success
Details 
Runtime: 1652 ms, faster than 57.89% of Python online submissions for Largest Component Size by Common Factor.
Memory Usage: 18.8 MB, less than 100.00% of Python online submissions for Largest Component Size by Common Factor.
'''

class UnionFind(object):
    def uf(self, n):
        self.uf = [i for i in range(n)]
        self.size = [1] * n

    def find(self, x):
        if self.uf[x] != x:
            self.uf[x] = self.find(self.uf[x])
        return self.uf[x]

    def union(self, x, y):
        x_root = self.find(x)
        y_root = self.find(y)
        if x_root == y_root:
            return
        self.uf[x_root] = y_root
        self.size[y_root] += self.size[x_root]
        self.size[x_root] = 0


class Solution(object):
    def largestComponentSize(self, A):
        """
        :type A: List[int]
        :rtype: int
        """

        def primeFactors(n):
            out = set()
            while n % 2 == 0:
                out.add(2)
                n //= 2
            for i in range(3, int(math.sqrt(n)) + 1, 2):
                while n % i == 0:
                    out.add(i)
                    n //= i
            if n > 2:
                out.add(n)
            return out

        idx_lookup = {A[i]: i for i in range(len(A))}
        uf = UnionFind()
        uf.uf(len(A))
        primesAndMultiples = collections.defaultdict(list)

        for num in A:
            factors_set = primeFactors(num)
            for f in factors_set:
                primesAndMultiples[f].append(num)

        for idx, multiples in primesAndMultiples.items():
            if multiples:
                root = multiples[0]
                for node in multiples[1:]:
                    uf.union(idx_lookup[node], idx_lookup[root])
        return max(uf.size)


