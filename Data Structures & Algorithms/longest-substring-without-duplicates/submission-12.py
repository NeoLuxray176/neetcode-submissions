class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res, curr = 0, 0
        left = 0
        last_occurances = {}

        for right, char in enumerate(s):
            if not char in last_occurances:
                last_occurances[char] = right
            else:
                left = last_occurances[char] + 1
                last_occurances.pop(char)

            res = max(res, right - left)

        return res

