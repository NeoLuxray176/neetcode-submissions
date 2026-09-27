class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        max_val = max(interval[0] for interval in intervals)

        mp = [0] * (max_val + 1)
        for start, end in intervals:
            # mp[i] is the maximum interval starting at i
            # i.e. it contains the maximum end value starting from i
            mp[start] = max(end + 1, mp[start])

        res = []
        interval_end = -1
        interval_start = -1
        for i in range((len(mp))):
            # An interval starts at index i
            if mp[i] != 0:
                if interval_start == -1:
                    interval_start = i
                # Choose the maximum end of this interval
                interval_end = max(mp[i] - 1, interval_end)
            if interval_end == i:
                # We have reached the end of this interval without ever seeing
                # an interval that extends it. (Otherwise we would have ended up in the if condition
                # above.)
                res.append([interval_start, interval_end])
                interval_end = -1
                interval_start = -1

        # Add the last remaining interval
        if interval_start != -1:
            res.append([interval_start, interval_end])

        return res