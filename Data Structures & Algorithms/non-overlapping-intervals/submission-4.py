class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        count = 0

        last_end = intervals[0][1]

        for start, end in intervals[1:]:
            if start < last_end:
                count += 1
                last_end = min(end, last_end)
            else:
                # last_end = min(end, last_end)
                last_end = end

        return count            
