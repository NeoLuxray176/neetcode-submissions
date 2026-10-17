class Solution:
    def numSquares(self, n: int) -> int:
        dp = list(range(n + 1))

        for i in range(n + 1):
            for j in range(n + 1):
                if i - j * j >= 0:
                    dp[i] = min(dp[i], 1 + dp[i - j * j])

        # print(dp)
        return dp[n]