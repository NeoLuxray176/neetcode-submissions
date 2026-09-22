class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        # Task
        # We actually want to minimize the difference between two sets of stones
        # Because once we start smashing them the difference between the sets
        # will always stay the same.

        stone_sum = sum(stones)
        target = stone_sum // 2
        n = len(stones)

        # i = how many stones are available
        # j = the current weight capacity
        # dp[i][j] = the best subset sum achievable with that capacity
        dp = [[0] * (target + 1) for _ in range(n + 1)]

        for i in range(1, n + 1):
            for j in range(1, target + 1):
                if stones[i - 1] > j:
                    dp[i][j] = dp[i - 1][j]
                else:
                    curr_stone_weight = stones[i - 1]
                    dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - curr_stone_weight] + curr_stone_weight)

        return stone_sum - 2 * dp[n][target]