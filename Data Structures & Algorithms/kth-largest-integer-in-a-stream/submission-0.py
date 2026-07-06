class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.arr = sorted(nums[:k+1], reverse=True)
        

    def add(self, val: int) -> int:
        self.arr.append(val)
        self.arr.sort()
        return self.arr[len(self.arr) - self.k]
        
