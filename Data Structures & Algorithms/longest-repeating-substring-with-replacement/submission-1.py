class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0

        left = 0
        maxf = 0

        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxf = max(maxf, count[s[r]])

            # Her left is never bigger than r, so we do have a proper substring
            # we shrink from the left by increasing l.
            while (r - left + 1) - maxf > k:
                count[s[left]] -= 1
                left += 1
            res = max(res, r - left + 1)
        
        return res