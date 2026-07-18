class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)

        # Start out with amount and subtract each of the coin values.
        # For each of these, we then again subtract each of the coins values
        # We repeat this until we reach zero (or don't)

        # We check at most the number of coins times the amount. This happens in the scenario
        # where we have a coin of value 1


        def dfs(target):
            if target == 0:
                return 0

            best = amount + 1
            for coin in coins:
                if target >= coin:
                    best = min(best, 1 + dfs(target - coin))
            
            return best

        res = dfs(amount)

        if res > amount:
            return -1
        else:
            return res

