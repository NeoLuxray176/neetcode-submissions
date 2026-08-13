from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        # State of a day, from the perspective of the start of that day:
        #   HOLDING -> a share is owned and may be sold
        #   FREE    -> nothing is owned and a share may be bought
        HOLDING = 0
        FREE = 1

        # dp[i][state] = maximum profit obtainable from day i onward,
        # given that we enter day i in `state`.
        #
        # Two padding rows serve as the base case (profit 0 once the days run
        # out). Two rather than one, because selling on day n - 1 skips the
        # cooldown day and reads dp[n + 1].
        dp = [[0, 0] for _ in range(n + 2)]

        # Filled backwards: dp[i] only ever depends on dp[i + 1] and dp[i + 2].
        for i in range(n - 1, -1, -1):
            # Entering day i with nothing owned.
            buy_today = dp[i + 1][HOLDING] - prices[i]
            stay_free = dp[i + 1][FREE]
            dp[i][FREE] = max(buy_today, stay_free)

            # Entering day i holding a share.
            # Day i + 1 is the mandatory cooldown, so trading resumes at i + 2.
            sell_today = dp[i + 2][FREE] + prices[i]
            keep_holding = dp[i + 1][HOLDING]
            dp[i][HOLDING] = max(sell_today, keep_holding)

        # Day 0: nothing owned yet.
        return dp[0][FREE]