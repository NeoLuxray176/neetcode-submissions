class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)

        # dp[i][j] true means that the string starting from i and ending at j
        # is a palindrome and false means it isn't
        dp = [[False] * n for _ in range(n)]


        start, length = 0, 1

        for i in range(n):
            dp[i][i] = True 


        for i in range(n - 1, -1 , -1):
            for j in range(i, n):
                if s[i] != s[j]:
                    continue

                if j - i <= 2 or dp[i + 1][j - 1]:
                    dp[i][j] = True

                    if j - i + 1 >= length:
                        start, length = i, j - i + 1
        
        return s[start : start + length]