class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return len(s) == len(t) and set(s) == set(t)