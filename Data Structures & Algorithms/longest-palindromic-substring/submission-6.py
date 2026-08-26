class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)

        # This is 2D dp[i][j] means that the substring s[i..j] is a palindrome
        # We only ever fill the upper triangle (i <= j)
        # Still both space and time complexity is O(n^2)
        dp = [[False] * n for _ in range(n)]

        # This is our current longest substring, a single character is
        # always a palindrome so length 1 is a safe starting point
        start, best = 0, 1

        # Every single character is trivially a palindrome, this is our base case
        for i in range(n):
            dp[i][i] = True

        # We go by increasing length so that dp[i + 1][j - 1] (which is exactly
        # two characters shorter) is guaranteed to be computed already
        for length in range(2, n + 1):
            # i is the start, j the end of the window of the current length
            for i in range(n - length + 1):
                j = i + length - 1

                # A palindrome must have matching characters at both ends,
                # otherwise there is nothing to check
                if s[i] != s[j]:
                    continue

                # Either the two matching characters are direct neighbors
                # (length == 2, so there is no inside left to check)
                # or
                # they extend a shorter palindrome by being equal, and we can
                # always extend a palindrome with two equal characters at each end
                if length == 2 or dp[i + 1][j - 1]:
                    # We first update our dp matrix
                    dp[i][j] = True

                    # We check if this is the new longest palindrome
                    if length > best:
                        start, best = i, length

        return s[start : start + best]