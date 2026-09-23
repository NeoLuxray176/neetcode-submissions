class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        n = len(s)
        res = set()

        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                for k in range(j + 1, n):
                    if s[i] != s[k]:
                        continue
                    res.add(s[i] + s[j] + s[k])
        
        return len(res)