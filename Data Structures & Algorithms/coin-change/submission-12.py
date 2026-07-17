class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        def recurse(target : int) -> int:
            if target == 0:
                return 0

            res = amount + 1

            for coin in coins:
                if coin <= target:
                    res = min(res, 1 + recurse(target - coin))
            
            return res

        res = recurse(amount)
        return -1 if res > amount else res