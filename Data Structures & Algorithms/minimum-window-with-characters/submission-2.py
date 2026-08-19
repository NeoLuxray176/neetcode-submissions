class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l, r = 0, 0
        res = []

        for c in range(len(s)):
            if s[c] in t:
                l, r = c, c
                target_copy = list(t)
                
                while r < len(s):
                    if s[r] in target_copy:
                        target_copy.remove(s[r])
                    if len(target_copy) == 0:
                        res.append(s[l:r+1])
                        break

                    r += 1
            
        if not res:
            return ""
        return min(res, key=len)