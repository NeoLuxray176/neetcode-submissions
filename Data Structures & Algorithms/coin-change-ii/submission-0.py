class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        coins.sort()

        n = len(coins)

        memo = [[-1] * (amount + 1) for _ in range(n + 1)]

        def dfs(i, amount):
            if amount == 0:
                return 1
            if i >= n:
                return 0
            if memo[i][amount] != -1:
                return memo[i][amount]

            res = 0

            if amount >= coins[i]:
                res += dfs(i + 1, amount)
                res += dfs(i, amount - coins[i])

            memo[i][amount] = res
            return res

        return dfs(0, amount)