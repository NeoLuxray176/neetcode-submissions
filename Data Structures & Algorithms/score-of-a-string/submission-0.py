class Solution:
    def scoreOfString(self, s: str) -> int:
        res = 0

        for i in range(1, (len(s))):
            a = ord("a") - ord(s[i - 1])
            b = ord("a") - ord(s[i])
            res += abs(b - a)

        return res
