class Solution:
    def maxScore(self, s: str) -> int:
        n = len(s)

        res = 0

        for i in range(1, n):
            left, right = s[:i], s[i:]
            # print(left, right)
            best = left.count("0") + right.count("1")
            res = max(res, best)

        return res