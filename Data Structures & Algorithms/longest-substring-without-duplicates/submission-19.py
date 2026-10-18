class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Task:
        # Longest substring without repeating characters
        # Constraints: None, remember to handle empty string
        # General Idea:
        # Iterate over string Keep track of the last occurance of each character, 
        # from that we can compute the longest substring on
        # the next occurance of that character
        # Refined Idea:
        # map that will contain the last occurance of each character
        # for i in range(len(s)):
        # if s[i] in mp:
        #   res = max(res, i - mp[s[i]] + 1)
        # mp[s[i]] = i
        #   
        # Test Vectors:  

        left = res = 0
        mp = {}

        for i in range(len(s)):
            if s[i] in mp:
                left = max(left, mp[s[i]] + 1)
            res = max(res, i - left + 1)
            mp[s[i]] = i

        return res