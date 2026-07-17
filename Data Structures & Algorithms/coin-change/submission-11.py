class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        def fewest_coins(remaining : int) -> int:
            if remaining == 0:
                return 0

            res = amount + 1
            for coin in coins:
                if coin <= remaining:
                    res = min(res, 1 + fewest_coins(remaining - coin))
            return res

        res = fewest_coins(amount)
        return res if res <= amount else -1
                    