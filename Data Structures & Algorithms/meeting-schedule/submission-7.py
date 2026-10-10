"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals:
            return True

        intervals.sort(key=lambda x : [x.start, x.end])

        last_end = intervals[0].end

        for interval in intervals[1:]:
            start, end = interval.start, interval.end
            if start < last_end:
                return False
            else:
                last_end = end

        return True