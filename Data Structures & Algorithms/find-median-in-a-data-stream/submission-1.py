class MedianFinder:

    def __init__(self):
        self.small, self.large = [], []
        self.size_small, self.size_large = 0, 0
        

    def addNum(self, num: int) -> None:
        if self.large and num > self.large[0]:
            heapq.heappush(self.large, num)
            self.size_large += 1
        else:
            heapq.heappush(self.small, -1 * num)
            self.size_small += 1

        if len(self.small) > len(self.large) + 1:
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)
            self.size_large += 1
            self.size_small -= 1
        if len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -1 * val)
            self.size_large -= 1
            self.size_small += 1
        

    def findMedian(self) -> float:
        if self.size_small > self.size_large:
            return -1 * self.small[0]
        elif self.size_large > self.size_small:
            return self.large[0]
        return (-1 * self.small[0] + self.large[0]) / 2.0
        
        