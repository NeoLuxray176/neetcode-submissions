class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        max_heap = nums
        heapq.heapify_max(max_heap)

        while k > 1:
            heapq.heappop_max(max_heap)
            k -= 1

        return max_heap[0]








