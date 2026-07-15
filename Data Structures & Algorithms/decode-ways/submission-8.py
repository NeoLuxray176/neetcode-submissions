class Solution:
    def numDecodings(self, s: str) -> int:
        
        def recurse(i):
            if i == len(s):
                return 1
            if s[i] == '0':
                return 0

            res = recurse(i + 1)
            if i < len(s) - 1:
                if (s[i] == '1' or (s[i] == '2' and s[i + 1] < '7')):
                    res += recurse(i + 2)

            return res

        return recurse(0)