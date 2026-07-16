class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        cache = [-1] * n

        def recurse(i):
            if i == n:
                return 1
            if s[i] == '0':
                return 0

            if cache[i] != -1:
                return cache[i]

            res = recurse(i + 1)
            if i < n - 1:
                if s[i] == '1' or (s[i] == "2" and s[i + 1] < "7"):
                    res += recurse(i + 2)
            
            cache[i] = res
            return res

        return recurse(0)