class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)

        res = 0
        dp = [0] * (n + 1)
        dp[n] = 1

        for i in range(n - 1, -1 , -1):
            curr = int(s[i])

            if curr == 0:
                dp[i] = 0
            else:
                dp[i] = dp[i + 1]

                if i < n - 1:
                    prev = int(s[i + 1])
                    if curr == 1 or (curr == 2 and prev <= 6):
                        dp[i] += dp[i + 2]

        return dp[0]