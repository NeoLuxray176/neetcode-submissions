class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        left, right = 0, 1
        res = 0

        while left < n and right < n:
            profit = prices[right] - prices[left]
            if profit < 0:
                left = right
            else:
                res = max(res, profit)
                right += 1

        return res