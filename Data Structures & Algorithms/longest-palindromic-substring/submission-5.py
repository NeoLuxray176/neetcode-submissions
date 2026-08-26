class Solution:
    def longestPalindrome(self, s: str) -> str:
        # This is our current longest substring
        resIdx, resLen = 0, 0
        n = len(s)

        # This is 2D dp[i][j] means that the substring s[i..j] is a palindrome
        # So we have a triangle that we cover.
        # Still both space and time complexity is O(n^2)
        dp = [[False] * n for _ in range(n)]

        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                # If the characters at i and j are the same then
                if s[i] == s[j]:
                    # either they form a triplet e.g. aba in the case == 2
                    # they are direct neighbors == 1 or theya re the same == 0
                    # or
                    # they extend a previous palindrome by being equal and we can always
                    # extend a palindrome with two equal characters at each end
                    if(j - i <= 2 or dp[i + 1][j - 1]):
                        # We first update our dp matrix
                        dp[i][j] = True
                        # We check if this is the new longest palindrome
                        if resLen < (j - i + 1):
                            resIdx = i
                            resLen = j - i + 1

        return s[resIdx : resIdx + resLen]