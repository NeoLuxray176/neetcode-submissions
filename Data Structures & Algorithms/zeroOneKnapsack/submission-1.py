class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        dp = [0] * (capacity + 1)

        for i in range(len(profit)):
            for j in range(capacity, weight[i] - 1, -1):
                if weight[i] > j:
                    dp[j] = dp[max(j - 1, 0)]
                    continue
                # Choose to include this item, or choose to not include this item
                dp[j] = max(dp[j], dp[j - weight[i]] + profit[i], dp[j - 1])

        return dp[capacity]
