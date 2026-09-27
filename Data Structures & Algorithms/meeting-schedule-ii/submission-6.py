"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda x: x.start)

        room_ends = []

        for interval in intervals:
            start, end = interval.start, interval.end
            needs_new_room = True
            for room_end in room_ends:
                if room_end <= start:
                    needs_new_room = False
            if needs_new_room:
                room_ends.append(end)

        return len(room_ends)
            
