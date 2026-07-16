class Solution:
    cache = {}
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # Greedy does not work because we could use a word that prevents a solution

        # Decision tree with one child per word in the dict
        # Use that word or use something else

        if not s:
            return True

        if s in self.cache:
            return self.cache[s]

        res = False
        for word in wordDict:
            if word in s:
                res = res or self.wordBreak(s[len(word):], wordDict)

                if res:
                    self.cache[s] = True

        return res