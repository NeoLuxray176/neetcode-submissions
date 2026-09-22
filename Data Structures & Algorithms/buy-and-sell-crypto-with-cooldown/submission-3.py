class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        HOLDING = 0
        FREE = 1

        dp = [[0, 0] for _ in range(n + 2)]

        for i in range(n - 1, -1 ,-1):
            buy_today = dp[i + 1][HOLDING] - prices[i]
            stay_free = dp[i + 1][FREE]
            dp[i][FREE] = max(buy_today, stay_free)

            sell_today = dp[i + 2][FREE] + prices[i]
            keep_holding = dp[i + 1][HOLDING]
            dp[i][HOLDING] = max(sell_today, keep_holding)

        return dp[0][FREE]