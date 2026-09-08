class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        map = {}
        left = 0
        res = 0

        for right in range(len(s)):
            if s[right] in map:
                left = max(map[s[right]] + 1, left)
            res = max(res, right - left + 1)
            map[s[right]] = right

        return res