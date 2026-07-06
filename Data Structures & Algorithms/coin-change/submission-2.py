class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # We cannot use greedy, e.g. we could have amount 12 and coins [1, 6, 10]
        # Starting at the back taking 10 would be a mistake
        
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        for curr_am in range(1, amount + 1):
            for curr_coin in coins:
                # If the current amount minus the current coin is smaller than zero
                # then we cannot use that coin for this amount
                if curr_am - curr_coin >= 0:
                    # Either we keep the minimal amount of used coins at the current amount
                    # OR we update and use the current coin for the current amount i.e. we increment by
                    # one since we us a new coin
                    dp[curr_am] = min(dp[curr_am], dp[curr_am - curr_coin] + 1)

        # We did not update the default value, so we cannot express this amount
        # with the coins that we were given
        if dp[amount] == amount + 1:
            return -1

        return dp[amount]
