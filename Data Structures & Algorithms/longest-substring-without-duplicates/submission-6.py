class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # We use a map to store the leftmost index of every character
        # upon encountering it agin we know where to set our left pointer
        # and can from the left pointer and the current position
        # calculate the current length of the substring
        
        map = {}
        left = 0
        res = 0

        for right in range(len(s)):
            if s[right] in map:
                left = max(map[s[right]] + 1, left)
            map[s[right]] = right
            res = max(res, right - left + 1)
        
        return res