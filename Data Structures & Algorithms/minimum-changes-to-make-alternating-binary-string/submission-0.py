class Solution:
    def minOperations(self, s: str) -> int:
        n = len(s)
        res = 0
        
        i = 1
        while i < n:
            print(s[i - 1], s[i])
            if s[i - 1] == s[i]:
                res += 1
                i += 1
            i += 1

        return res