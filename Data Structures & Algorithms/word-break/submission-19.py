from functools import cache

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)

        @cache
        def recurse(start : int) -> bool:
            if start > n:
                return False
            if start == n:
                return True

            for word in wordDict:
                if s[start:].startswith(word):
                    if recurse(start + len(word)):
                        return True

            return False

        if recurse(0):
            return True
        return False