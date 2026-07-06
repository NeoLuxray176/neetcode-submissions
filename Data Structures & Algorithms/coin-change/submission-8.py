class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if len(coins) == 1:
            if amount % coins[0] != 0:
                return -1
        
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        for i in range(amount + 1):
            for coin in coins:
                if i - coin >= 0:
                    dp[i] = min(dp[i], dp[i - coin] + 1)
        
        if dp[amount] == amount + 1:
            return -1

        return dp[amount]