class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # General idea
        # For each index in each of the strings we want to know what the currenlty longest
        # common subsequence is, from that we can then expand to the next index

        n, m = len(text1), len(text2)

        dp = [[0] * (m + 1) for _ in range(n + 1)]

        for i in range(n):
            for j in range(m):
                if text1[i] == text2[j]:
                    dp[i + 1][j + 1] = 1 + dp[i][j]
                else:
                    dp[i + 1][j + 1] = max(dp[i + 1][j], dp[i][j + 1])

        return dp[n][m]