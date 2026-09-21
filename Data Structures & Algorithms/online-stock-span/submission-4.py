class StockSpanner:

    def __init__(self):
        self.stack = []
        

    def next(self, price: int) -> int:
        i = 1
        while self.stack and self.stack[-1][0] <= price:
            _ , j = self.stack.pop()
            i += j
        self.stack.append([price, i])

        return i
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)