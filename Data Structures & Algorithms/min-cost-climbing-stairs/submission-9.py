class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        if n == 1:
            return cost[0]
        if n == 2:
            return min(cost[0], cost[1])

        arr = [0] * n
        arr[0] = cost[0]
        arr[1] = cost[1]

        for i in range(2, n):
            arr[i] = min(arr[i - 1] + cost[i - 1], arr[i - 2] + cost[i - 2])

        return arr[-1]