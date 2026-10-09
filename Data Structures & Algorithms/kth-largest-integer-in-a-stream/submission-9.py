class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.limit = k
        self.heap = []
        for val in nums:
            # heapq.heappush(self.heap, val)
            self.add(val)
        
        

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        while len(self.heap) > self.limit:
            heapq.heappop(self.heap)
        
        print(self.heap)
        return self.heap[0]
        
