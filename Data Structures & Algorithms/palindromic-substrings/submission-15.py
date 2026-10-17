class Solution:
    def countSubstrings(self, s: str) -> int:
        

        def expand_around(i : int) -> int:
            res = 0
            for left, right in [[i, i + 1], [i, i + 2]]:
                curr = s[left:right]
                cand = curr[::-1]

                while left >= 0 and right <= len(s) and curr == cand:
                    # print(curr, cand)
                    res += 1
                    left -= 1
                    right += 1
                    curr = s[left:right+1]
                    cand = curr[::-1]
            # print(f"For center {i} return {res}")
            return res

        res = 0
        for center in range(len(s)):
            res += expand_around(center)

        return res