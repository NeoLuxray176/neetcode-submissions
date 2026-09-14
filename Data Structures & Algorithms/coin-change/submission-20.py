class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [-1] * (amount + 1)
        dp[0] = 0

        for i in range(amount + 1):
            for coin in coins:
                if i - coin >= 0 and dp[i - coin] != -1:
                    candidate = dp[i - coin] + 1

                    if dp[i] == -1:
                        dp[i] = candidate
                    else:
                        dp[i] = min(dp[i], candidate)

        return dp[amount]