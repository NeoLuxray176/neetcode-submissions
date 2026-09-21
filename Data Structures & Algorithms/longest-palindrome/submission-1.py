class Solution:
    def longestPalindrome(self, s: str) -> int:
        hmap = {}

        for character in s:
            if character in hmap:
                hmap[character] += 1
            else:
                hmap[character] = 1

        res = 0
        odd_used = False

        for value in hmap.values():
            if value % 2 == 0:
                res += value
            elif not odd_used:
                res += value
                odd_used = True
            else:
                res += (value - 1)
        
        return res
