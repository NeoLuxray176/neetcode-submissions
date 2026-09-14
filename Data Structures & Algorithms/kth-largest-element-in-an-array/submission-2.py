class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify_max(nums)

        while k > 1:
            interm = heapq.heappop_max(nums)
            k -= 1

        return heapq.heappop_max(nums)