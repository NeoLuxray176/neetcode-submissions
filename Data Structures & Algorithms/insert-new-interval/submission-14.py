class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        n = len(intervals)
        res = []
        i = 0

        # interval ends before new interval starts, they cannot overlap
        while i < n and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i += 1

        # interval ends after (or equal) to when newInterval starts
        start = newInterval[0]
        end = newInterval[1]
        while i < n and intervals[i][0] < end:
            start = min(start, intervals[i][0])
            end = max(end, intervals[i][1])
            i += 1

        res.append([start, end])
        res += intervals[i:]

        return res