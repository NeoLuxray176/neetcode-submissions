class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [1] * n
        # dp[n-1] = 1

        for i in range(n - 2, -1, -1):
            if s[i] == "1" and s[i + 1] in ["0123456789"]:
                dp[i] = dp[i] + dp[i + 1]

            if s[i] == "2" and s[i + 1] in  ["123456"]:
                dp[i] = dp[i] + dp[i + 1]

        return dp[0]