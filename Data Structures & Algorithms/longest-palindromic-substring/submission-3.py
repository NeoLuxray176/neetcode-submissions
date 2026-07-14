class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        
        res, resLen = "", 0

        for i in range(n):
            for j in range(i, n):
                left, right = i, j
                while left < right and s[left] == s[right]:
                    left += 1
                    right -= 1

                if left >= right and resLen < (j - i + 1):
                    res = s[i : j + 1]
                    resLen = j - i +1
        
        return res
