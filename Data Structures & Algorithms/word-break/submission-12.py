class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)

        def recurse(s : str) -> bool:
            if not s:
                return True

            res = False
            for word in wordDict:
                if s.startswith(word):
                    res =  res or recurse(s[len(word):])

            return res

        res = recurse(s)
        return res
