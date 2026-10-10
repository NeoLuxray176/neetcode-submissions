"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        heap = []
        res = 0

        intervals.sort(key = lambda x : [x.start, x.end])

        for interval in intervals:
            while heap and heap[0] <= interval.start:
                    heapq.heappop(heap)
                    
            if not heap or heap[0] > interval.start:
                heapq.heappush(heap, interval.end)
                
            

            res = max(res, len(heap))

        return res
