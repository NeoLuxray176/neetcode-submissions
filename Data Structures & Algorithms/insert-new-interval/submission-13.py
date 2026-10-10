class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        n = len(intervals)
        res = []
        i = 0

        # Add all intervals that end before ours starts to the result
        while i < len(intervals) and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i += 1
        
        # Now we know that the next interval in the array ends after the
        # new interval starts
        new_start = newInterval[0]
        new_end = newInterval[1]
        while i < n and intervals[i][0] <= new_end:
            new_start = min(new_start, intervals[i][0])
            new_end = max(new_end, intervals[i][1])
            i += 1

        res.append([new_start, new_end])

        while i < n:
            res.append(intervals[i])
            i += 1

        return res

        