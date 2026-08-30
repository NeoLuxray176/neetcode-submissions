class Solution:
    def countSubstrings(self, s: str) -> int:
        # This is just the same code as the previous task
        # but this time we also count the number of palindromes we find
        n, res = len(s), 0
        dp = [[False] * n for _ in range(n)]

        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j - i <= 2 or dp[i + 1][j - 1]):
                    dp[i][j] = True
                    res += 1

        return res