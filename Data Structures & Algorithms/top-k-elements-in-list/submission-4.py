class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dictionary = {}

        for num in nums:
            if num in dictionary:
                dictionary[num] += 1
            else:
                dictionary[num] = 1

        heap = []

        for key, value in dictionary.items():
            heapq.heappush(heap, [value, key])

            if len(heap) > k:
                heapq.heappop(heap)

        res = []

        for value, key in heap:
            res.append(key)

        return res