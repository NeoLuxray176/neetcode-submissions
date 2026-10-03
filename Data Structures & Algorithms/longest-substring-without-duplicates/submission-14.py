class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        last_occurance = {}

        best = -1

        for i in range(len(s)):
            if s[i] in last_occurance:
                best = max(best, i - last_occurance[s[i]])
            last_occurance[s[i]] = i

        if best < 0:
            return len(s)
        else:
            return best

