'''
https://leetcode.com/problems/number-of-atoms/
'''


class Solution(object):
    def countOfAtoms(self, formula):
        """
        :type formula: str
        :rtype: str
        """

        def parse(i, mult=1):
            while i >= 0 and '(' != formula[i]:
                count, power = 0, 1
                while formula[i].isdigit():
                    count = (power * int(formula[i])) + count
                    i -= 1
                    power *= 10
                # count at least 1
                count = max(count, 1)

                if ')' == formula[i]:
                    # i need to be changed
                    i = parse(i - 1, count * mult)
                    continue

                name = []
                while formula[i].islower():
                    name += formula[i]
                    i -= 1
                # add  the first Upper case letter
                name += formula[i]
                dicts[''.join(name[::-1])] += count * mult
                i -= 1
            return i - 1

        dicts = collections.defaultdict(int)
        parse(len(formula) - 1)
        print(dicts)

        ans = ""
        for el, count in sorted(dicts.items()):
            ans += el + (str(count) if count > 1 else "")
        return ans

'''
Success
Details 
Runtime: 20 ms, faster than 78.42% of Python online submissions for Number of Atoms.
Memory Usage: 13 MB, less than 100.00% of Python online submissions for Number of Atoms.
'''
