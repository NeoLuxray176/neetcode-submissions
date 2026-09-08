class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        curr_chars = set()
        res = 0

        for character in s:
            if character not in curr_chars:
                curr_chars.add(character)
                res = max(res, len(curr_chars))
            else:
                curr_chars = set()
                curr_chars.add(character)

        return res