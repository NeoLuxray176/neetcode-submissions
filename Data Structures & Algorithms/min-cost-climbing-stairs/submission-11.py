class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)

        if n == 0:
            return 0
        if n == 1:
            return cost[0]
        if n == 2:
            return min(cost[0], cost[1])

        arr = [0] * (n + 1)
        # This is not needed because we can start at either 0 or 1 free of cost.
        # arr[0], arr[1] = cost[0], min(cost[0], cost[1])

        for i in range(2, n + 1):
            arr[i] = min(arr[i - 1] + cost[i - 1], arr[i - 2] + cost[i - 2])

        return arr[n]