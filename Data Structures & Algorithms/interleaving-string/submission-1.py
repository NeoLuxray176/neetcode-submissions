class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n, m = len(s1), len(s2)

        if len(s3) != n + m:
            return False

        # dp[i][j] is True if we can use the first i characters from s1 and the first j characters from s2 to build
        # the first i + j characters of s3
        dp = [[False] * (m + 1) for _ in range(n + 1)]

        dp[0][0] = True

        for i in range(n + 1):
            for j in range(m + 1):
                if i > 0 and s1[i - 1] == s3[i + j - 1]:
                    dp[i][j] |= dp[i - 1][j]
                if j > 0 and s2[j - 1] == s3[i + j - 1]:
                    dp[i][j] |= dp[i][j - 1]

        return dp[-1][-1]