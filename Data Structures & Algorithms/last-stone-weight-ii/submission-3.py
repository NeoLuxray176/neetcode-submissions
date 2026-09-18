class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        # Task
        # We actually want to minimize the difference between two sets of stones
        # Because once we start smashing them the difference between the sets
        # will always stay the same.

        stone_sum = sum(stones)
        target = stone_sum // 2
        n = len(stones)

        dp = [[0] * (target + 1) for _ in range(n + 1)]

        for i in range(1, n + 1):
            for t in range(target + 1):
                if t >= stones[i - 1]:
                    dp[i][t] = max(dp[i - 1][t], dp[i - 1][t - stones[i - 1]] + stones[i - 1])
                else:
                    dp[i][t] = dp[i - 1][t]

        return stone_sum - 2 * dp[n][target]