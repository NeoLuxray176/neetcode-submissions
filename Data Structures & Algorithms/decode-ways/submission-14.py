class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [0] * (n + 1)
        dp[n] = 1

        for i in range(n - 1, -1, -1):
            if int(s[i]) == 0:
                dp[i] = 0
                continue

            dp[i] = dp[i + 1]
            
            if i < n - 1:
                if int(s[i]) == 1 or (int(s[i]) == 2 and int(s[i + 1]) <= 6):
                    dp[i] += dp[i + 2]

        return dp[0]