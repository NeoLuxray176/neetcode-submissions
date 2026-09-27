class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []

        intervals.sort()

        start = intervals[0][0]
        end = intervals[0][1]
        for interval in intervals:
            # Intervals are overlapping if the end of the previous interval is larger than
            # the start of the current interval
            if end >= interval[0]:
                start = min(start, interval[0])
                end = max(end, interval[1])
            else:
                res.append([start, end])
                start = interval[0]
                end = interval[1]

        res.append([start, end])
        return res
