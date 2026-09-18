class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        # Task
        # We actually want to minimize the difference between two sets of stones
        # Because once we start smashing them the difference between the sets
        # will always stay the same.

        stone_sum = sum(stones)
        target = stone_sum // 2

        dp = {}

        def dfs(i : int, total : int) -> int:
            if total >= target or i == len(stones):
                return abs(2 * total - stone_sum)

            if (i, total) in dp:
                return dp[(i, total)]

            dp[(i, total)] = min(dfs(i + 1, total + stones[i]), dfs(i + 1, total))
            return dp[(i, total)]

        return dfs(0, 0)