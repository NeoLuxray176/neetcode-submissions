"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        arr = []

        for interval in intervals:
            arr.append((interval.start, interval.end))

        arr.sort()
        # print(arr)

        i = 0
        while i < len(arr) - 1:
            if arr[i][1] > arr[i + 1][0]:
                return False
            i += 1

        return True
            