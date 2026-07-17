class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        cache = [-1] * (amount + 1)
        
        def recurse(target : int) -> int:
            if target == 0:
                return 0

            if cache[target] != -1:
                return cache[target]

            res = amount + 1

            for coin in coins:
                if coin <= target:
                    res = min(res, 1 + recurse(target - coin))
            
            cache[target] = res
            return res

        res = recurse(amount)
        return -1 if res > amount else res