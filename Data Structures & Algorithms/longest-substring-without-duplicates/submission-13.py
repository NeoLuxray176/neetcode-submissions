class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        left = 0
        last_occurances = {}

        for right, char in enumerate(s):
            # print(left, right)
            if not char in last_occurances:
                last_occurances[char] = right
            else:
                left = max(left, last_occurances[char] + 1)
                last_occurances.pop(char)
            last_occurances[char] = right

            res = max(res, right - left + 1)

        return res

