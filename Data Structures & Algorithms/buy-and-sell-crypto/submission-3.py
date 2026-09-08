class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, right = 0, 1
        max_profit = 0

        while right < len(prices):
            if prices[right] - prices[left] > 0:
                # We can make a profit
                max_profit = max(max_profit, prices[right] - prices[left])
            else:
                # We couldn't make a profit with the current value of left, i.e.
                # prices[right] is strictly smaller than prices[left] so choosing
                # prices[right] instead of prices[left] means we will make a bigger profit
                # in the future for sure
                left = right
            right = right + 1

        return max_profit