class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        cache = [-1] * (amount + 1)

        def fewest_coins(remaining):
            if remaining == 0:
                return 0

            if cache[remaining] != -1:
                return cache[remaining]
            
            best = amount + 1
            for coin in coins:
                if coin <= remaining:
                    best = min(best, 1 + fewest_coins(remaining - coin))

            cache[remaining] = best
            return best

        result = fewest_coins(amount)
        return -1 if result > amount else result
