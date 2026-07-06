class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        for a in range(1, amount + 1):
            for c in coins:
                if a - c >= 0:
                    # We can reach this amount either with a smaller amount of previous coins
                    # or by using the current coin a and a previously calculated amount of coins which
                    # we stored at dp[a - c]
                    dp[a] = min(dp[a], 1 + dp[a - c])

        # This is still the initial value, then we cannot reach the target amount
        if dp[amount] == amount + 1:
            return -1

        return dp[amount]