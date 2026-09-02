class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # Sort lexicographically: primarily by start, tie-broken by end.
        # Processing in start order means that once we pass an interval,
        # no later interval can start before it — so a single left-to-right
        # sweep is enough.
        intervals.sort()

        # Number of intervals removed so far.
        res = 0

        # Right endpoint of the last interval we decided to KEEP.
        # Everything to the left of this is already resolved.
        prevEnd = intervals[0][1]

        for start, end in intervals[1:]:
            # Half-open convention: touching at a point ([1,2] and [2,3])
            # does not count as overlapping.
            if start >= prevEnd:
                # Disjoint from the kept prefix — keep it, extend the frontier.
                prevEnd = end
            else:
                # Overlap. Exactly one of the two intervals must go, and
                # removing one is always sufficient here, so res grows by 1
                # regardless of which we discard.
                res += 1
                # Greedy choice: keep whichever ends earlier. A smaller
                # right endpoint is never worse — it constrains no future
                # interval that the larger one wouldn't also constrain
                # (exchange argument). Hence the min.
                prevEnd = min(end, prevEnd)

        return res