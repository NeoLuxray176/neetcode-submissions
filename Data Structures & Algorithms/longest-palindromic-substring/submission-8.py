class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)

        dp = [[False] * n for _ in range(n)]

        start, best = 0, 1

        for i in range(n):
            dp[i][i] = True

        for i in range(n - 1, -1 , -1):
            for j in range(i, n):
                if s[i] != s[j]:
                    continue

                if j - i <= 2 or dp[i + 1][j - 1]:
                    dp[i][j] = True
                    
                    if j - i + 1 >= best:
                        start = i
                        best = j - i + 1


        return s[start:start+best]