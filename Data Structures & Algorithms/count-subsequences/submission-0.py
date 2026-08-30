class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        # If t is longer than s, it cannot possibly be a subsequence of s.
        if len(t) > len(s):
            return 0

        # dp[(i, j)] = number of distinct ways to form t[j:] using s[i:].
        # Memoized recursion avoids recomputing overlapping subproblems.
        dp = {}

        def dfs(i, j):
            # Base case: t is fully matched (j reached the end of t) —
            # this counts as exactly one valid way, regardless of what's
            # left in s.
            if j == len(t):
                return 1
            # Base case: s is exhausted but t is not — no way to match
            # the remaining characters of t.
            if i == len(s):
                return 0
            # Return cached result if this subproblem was already solved.
            if (i, j) in dp:
                return dp[(i, j)]

            # Option 1: skip s[i] and try to match t[j:] against s[i+1:].
            # This is always a valid choice, since we're free to not use
            # s[i] as part of the subsequence.
            res = dfs(i + 1, j)

            # Option 2: if s[i] matches t[j], we can also *use* s[i] to
            # match t[j], and recurse on the remainder of both strings.
            # Both options are added together because they represent
            # distinct ways of building the subsequence.
            if s[i] == t[j]:
                res += dfs(i + 1, j + 1)

            # Cache and return the result for this (i, j) pair.
            dp[(i, j)] = res
            return res

        # Start matching from the beginning of both strings.
        return dfs(0, 0)