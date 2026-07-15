class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        res = n

        for i in range(n):
            left, right = i - 1, i + 1
            if left < 0 and right >= n:
                continue
            
            while left >= 0 and right < n and s[left] == s[right]:
                left, right = left - 1, right + 1
                res += 1

            left, right = i, i + 1
            if left < 0 and right >= n:
                continue
            
            while left >= 0 and right < n and s[left] == s[right]:
                left, right = left - 1, right + 1
                res += 1

        return res