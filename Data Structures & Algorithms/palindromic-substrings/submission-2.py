class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)

        res = n

        for i in range(n):
            j, k = i, i + 1
            while j >= 0 and k < n:
                if s[j] == s[k]:
                    res += 1
                j -= 1
                k += 1

            j, k = i - 1, i + 1
            while j >= 0 and k < n:
                if s[j] == s[k]:
                    res += 1
                j -= 1
                k += 1

        return res