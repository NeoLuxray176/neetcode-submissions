class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        map = {}
        left = 0
        res = 0

        for right in range(len(s)):
            if s[right] in map:
                left = map[s[right]] + 1
            res = max(res, right - left + 1)
            map[s[right]] = right

        return res