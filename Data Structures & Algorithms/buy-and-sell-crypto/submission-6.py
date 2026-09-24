class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        cheapest = float("inf")

        for price in prices:
            profit = max(profit, price - cheapest)
            cheapest = min(cheapest, price)

        return profit