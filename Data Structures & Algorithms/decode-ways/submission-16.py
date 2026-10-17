class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [0] * n

        for i in range(n - 1, -1, -1):
            if 0 < int(s[i]):
                dp[i] += 1
            if i < n - 1 and (int(s[i]) == 1 or (int(s[i]) == 2 and int(s[i + 1]) <= 6)):
                dp[i] += dp[i + 1]

        return dp[0]
            