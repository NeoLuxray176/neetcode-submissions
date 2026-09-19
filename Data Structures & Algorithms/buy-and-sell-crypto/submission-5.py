class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # General Idea
        # We want to find the maximum profit we can achieve by one buy and sell decision
        # So we buy immediately and check all future profits, if profits turn negative then we
        # have found a cheaper price to buy and replace the buy time.
        # In the mean time store the maximum profit achieved for all previous selling opportunities
        
        if not prices:
            return 0

        n = len(prices)
        res = 0
        curr = prices[0]

        for price in prices:
            profit = price - curr
            # print(price, curr, profit)
            if profit < 0:
                curr = price
            
            res = max(res, profit)

        return res