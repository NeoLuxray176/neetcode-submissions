class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(center : int) -> List[any]:
            res = ""
            for left, right in [[center, center], [center, center + 1]]:
                while left >= 0 and right < len(s) and s[left] == s[right]:
                    if len(res) < len(s[left:right+1]):
                        res = s[left:right+1]
                    
                    left -= 1
                    right += 1
            return res

        res = ""
        for center in range(len(s)):
            curr = expand(center)
            if len(curr) > len(res):
                res = curr


        return res