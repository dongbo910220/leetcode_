class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s or len(s) == 0:
            return False

        numSeen = False
        dotSeen = False
        eSeen = False

        s = s.strip()
        print(s)
        for i in range(len(s)):
            if s[i] >= '0' and s[i] <= '9':
                numSeen = True
            elif s[i] == '.':
                if dotSeen or eSeen:
                    return False
                dotSeen = True
            elif s[i] == 'e' or s[i] == 'E':
                print("e used")
                if eSeen or not numSeen:
                    return False
                eSeen = True
                numSeen = False
            elif s[i] == '-' or s[i] == '+':
                if i != 0 and s[i - 1] != 'e' and s[i - 1] != 'E':
                    return False
            else:
                return False
        return numSeen

s = Solution
print(s.isNumber(s,"e"))