"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        n = len(intervals)
        dp = [-1] * n

        for interval in intervals:
            start, end = interval.start, interval.end
            for i in range(n):
                # print(f"Checking room {i} {dp[i]} {start}")
                if dp[i] < start:
                    # print(f"Use room {i} until {end}")
                    dp[i] = end
                    break
            
        res = 0
        for i in range(n):
            if dp[i] != -1:
                res += 1

        return res