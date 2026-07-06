class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mp = {}
        l = 0
        res = 0

        for r in range(len(s)):
            # If this is a repeat then we have to update the left pointer to where this character appeared
            # Note that we can never have a longer sequence with anything that includes the previous
            # appearance of this character
            if s[r] in mp:
                l = max(mp[s[r]] + 1, l)
            # This is the new updated position of this character
            # Note that we will never overwrite anything meaningful here because 
            # there are never any duplicates in the string as per the if condition above
            mp[s[r]] = r
            # Update the maximum length
            res = max(res, r - l  + 1)
        return res
