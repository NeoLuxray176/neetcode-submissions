class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n, m = len(word1), len(word2)

        # dp[i][j] stores the number of edits we have made after having
        #  processed i characters from word1 and j characters from word2
        dp = [[float("inf")] * (m + 1) for _ in range(n + 1)]

        for j in range(m + 1):
            dp[0][j] = j
        for i in range(n + 1):
            dp[i][0] = i

        for i in range(n):
            for j in range(m):
                if word1[i] == word2[j]:
                    dp[i + 1][j + 1] = dp[i][j]
                else:
                    dp[i + 1][j + 1] = 1 + min(dp[i][j + 1], dp[i + 1][j], dp[i][j])

        # for i in range(n):
            # print(dp[i])
        return dp[n][m]
