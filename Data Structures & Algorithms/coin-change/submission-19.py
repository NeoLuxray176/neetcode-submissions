class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        

        dp = [amount + 1] * (amount + 1)

        dp[0] = 0

        for i in range(amount + 1):
            for coin in coins:
                if dp[i] != amount + 1:
                    if i + coin < amount + 1:
                        dp[i + coin] = min(dp[i + coin], dp[i] + 1)

        if dp[amount] == amount + 1:
            return -1
        else:
            return dp[amount]