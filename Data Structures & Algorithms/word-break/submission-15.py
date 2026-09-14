class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if not hasattr(self, "cache"):
            self.cache = {}

        if not s:
            return True

        if s in self.cache:
            return self.cache[s]

        res = False
        for word in wordDict:
            if s.startswith(word):
                res = res or self.wordBreak(s[len(word):], wordDict)

        self.cache[s] = res

        return res