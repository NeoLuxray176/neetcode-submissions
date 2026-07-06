class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # Choose whether to start on the 0th or 1th step
        # Find cheapest way to the top, if we don't land at the top it doesn't count
        # e.g. if we take a two step step

        # [1, 2, 3, 4]
        
        n = len(cost)
        dp = [0] * (n+1)

        # dp[0], dp[1] = cost[0], cost[1]

        for i in range(2, n+1):
            dp[i] = min(dp[i-1] + cost[i - 1], dp[i-2] + cost[i-2])
        
        return dp[-1]