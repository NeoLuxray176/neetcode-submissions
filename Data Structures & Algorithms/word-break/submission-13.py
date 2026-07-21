class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)

        cache = {}

        def recurse(s : str) -> bool:
            if not s:
                return True

            if s in cache:
                return cache[s]

            res = False
            for word in wordDict:
                if s.startswith(word):
                    res =  res or recurse(s[len(word):])

            cache[s] = res

            return res

        res = recurse(s)
        return res
