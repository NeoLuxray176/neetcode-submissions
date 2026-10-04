class Solution:
    def maxScore(self, s: str) -> int:
        res = 0
        for i in range(1, len(s)):
            # print(f"{s[:i]} {s[i:]}")
            a = s[:i].count("0")
            b = s[i:].count("1")
            res = max(res, a + b)

        return res