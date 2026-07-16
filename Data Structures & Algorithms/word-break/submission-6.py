class Solution:
    cache = {}
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # Greedy does not work because we could use a word that prevents a solution

        # Decision tree with one child per word in the dict
        # Use that word or use something else

        n = len(s)

        wordSet = set(wordDict)

        cache = [-1] * n

        

        def dfs(i):
            if i == n:
                return True

            if cache[i] != -1:
                return cache[i]

            res = False
            for j in range(i, n):
                if s[i : j + 1] in wordSet:
                    if dfs(j + 1):
                        res = True

            cache[i] = res
            return res

        return dfs(0)