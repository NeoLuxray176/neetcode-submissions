class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        intervals.sort()

        start = intervals[0][0]
        end = intervals[0][1]
        for interval in intervals:
            # Next interval starts before the previous has ended
            if interval[0] <= end:
                start = min(interval[0], start)
                end = max(interval[1], end)
            # The intervals do not overlap
            else:
                res.append([start, end])
                start = interval[0]
                end = interval[1]

        res.append([start, end])

        return res

