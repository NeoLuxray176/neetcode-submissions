class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)

        dp = [amount + 1] * (amount + 1)
        dp[0] = 0


        for coin in coins:
            for j in range(amount + 1):
                if j - coin >= 0:
                    dp[j] = min(dp[j], dp[j - coin] + 1)

        if dp[amount] == amount + 1:
            return -1
        
        return dp[amount]