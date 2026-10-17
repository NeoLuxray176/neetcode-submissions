class Solution:
    def countSubstrings(self, s: str) -> int:
        def expand(center : int):
            res = 0
            for left, right in [[center, center], [center, center + 1]]:
                while left >= 0 and right < len(s) and s[left] == s[right]:
                    res += 1
                    left -= 1
                    right += 1
            return res

        res = 0
        for center in range(len(s)):
            res += expand(center)

        return res