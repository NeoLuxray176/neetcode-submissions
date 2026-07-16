class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        def fewest_coins(remaining):
            if remaining == 0:
                return 0
            best = amount + 1
            for coin in coins:
                if coin <= remaining:
                    best = min(best, 1 + fewest_coins(remaining - coin))
            return best

        result = fewest_coins(amount)
        return -1 if result > amount else result
