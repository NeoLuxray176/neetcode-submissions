"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # Sweep-line approach: instead of reasoning about intervals as objects,
        # decompose each meeting into two point events on the timeline.
        time = []
        for i in intervals:
            time.append((i.start, 1))   # a meeting starts -> one more room needed
            time.append((i.end, -1))    # a meeting ends   -> one room freed

        # Sort chronologically. The second sort key matters for ties: at an equal
        # timestamp, -1 (end) sorts before +1 (start), so a meeting ending at t
        # releases its room to a meeting starting at t. Intervals are treated as
        # half-open [start, end), which is what the problem wants.
        time.sort(key=lambda x: (x[0], x[1]))

        res = count = 0
        for t in time:
            # count = number of meetings currently in progress at this instant
            count += t[1]
            # the answer is the peak concurrency over the whole timeline
            res = max(res, count)
        return res