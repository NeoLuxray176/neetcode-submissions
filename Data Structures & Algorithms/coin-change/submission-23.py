class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)

        dp = [n + 1] * (amount + 1)
        dp[0] = 0


        for i in range(1, amount + 1):
            for coin in coins:
                if i - coin >= 0:
                    dp[i] = min(dp[i], 1 + dp[i - coin])

        if dp[amount] == n + 1:
            return -1
        return dp[amount]