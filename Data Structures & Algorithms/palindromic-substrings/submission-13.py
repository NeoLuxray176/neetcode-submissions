class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        res = n

        dp = [[False] * n for _ in range(n)]

        for i in range(n):
            dp[i][i] = True

        for i in range(n - 1 - 1, -1, -1):
            for j in range(i + 1, n):
                if s[i] != s[j]:
                    continue

                if j - i <= 2 or dp[i + 1][j - 1]:
                    res += 1
                    dp[i][j] = True

        return res