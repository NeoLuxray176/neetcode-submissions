class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)

        def try_from(curr_s : str) -> bool:
            if not curr_s:
                return True

            res = False
            for word in wordDict:
                if curr_s.startswith(word):
                    res = res or try_from(curr_s[len(word):])

            return res

        res = try_from(s)

        return res
                    