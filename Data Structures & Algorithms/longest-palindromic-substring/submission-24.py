class Solution:
    def longestPalindrome(self, s: str) -> str:
        def isPali(s):
            left, right = 0, len(s) - 1
            while left <= right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True

        n = len(s)

        dp = [[False] * n for _ in range(n)]

        start, length = 0, 1

        for i in range(n):
            dp[i][i] = True

        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if s[i] != s[j]:
                    continue
                
                if j - i <= 2 or dp[i + 1][j - 1]:
                    dp[i][j] = True
                
                    if j - i + 1 >= length:
                        start, length = i, j - i + 1

        return s[start : start + length]


        