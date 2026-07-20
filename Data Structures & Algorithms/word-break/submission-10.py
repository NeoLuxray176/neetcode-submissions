class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)

        cache = {}

        def try_from(curr_s : str) -> bool:
            if not curr_s:
                return True

            if curr_s in cache:
                return cache[curr_s]

            res = False
            for word in wordDict:
                if curr_s.startswith(word):
                    res = res or try_from(curr_s[len(word):])

            cache[curr_s] = res

            return res

        res = try_from(s)

        return res
                    