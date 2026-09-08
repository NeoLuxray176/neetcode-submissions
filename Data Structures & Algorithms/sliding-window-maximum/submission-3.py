class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap = []
        res = []

        for i in range(len(nums)):
            # Push the items onto the heap (remember this is a min heap so we put the negative 
            # of the actual value here)
            heapq.heappush(heap, (-nums[i], i))
            # if i + 1 >= k:
            if k <= i + 1:
                # pop items until we have reached the largest element in the current interval
                while heap[0][1] <= i - k:
                    heapq.heappop(heap)
                # The largest element in the current interval
                res.append(-heap[0][0])
        
        return res