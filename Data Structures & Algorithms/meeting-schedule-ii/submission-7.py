"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0

        intervals.sort(key=lambda x: x.start)

        room_ends = []

        for interval in intervals:
            start, end = interval.start, interval.end
            if room_ends and room_ends[0] <= start:
                heapq.heappop(room_ends)
            heapq.heappush(room_ends, end)

        return len(room_ends)
