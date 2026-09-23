import heapq
from typing import List

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        # Store: enqueue time, processing time, original index
        arr = [
            (enqueue, processing, index)
            for index, (enqueue, processing) in enumerate(tasks)
        ]

        # Tasks are processed in enqueue-time order
        arr.sort(key=lambda task: task[0])

        result = []
        available = []

        i = 0
        time = arr[0][0]

        while i < len(arr) or available:
            # Add every task that has become available
            while i < len(arr) and arr[i][0] <= time:
                enqueue, processing, index = arr[i]
                heapq.heappush(available, (processing, index))
                i += 1

            if available:
                processing, index = heapq.heappop(available)
                result.append(index)
                time += processing
            else:
                # CPU is idle until the next task arrives
                time = arr[i][0]

        return result