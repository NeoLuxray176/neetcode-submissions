class Solution:
    cache = {}
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # Greedy does not work because we could use a word that prevents a solution

        # Decision tree with one child per word in the dict
        # Use that word or use something else

        wordSet = set(wordDict)

        n = len(s)

        def dfs(i):
            if i == n:
                return True

            for j in range(i, n):
                if s[i : j + 1] in wordSet:
                    if dfs(j + 1):
                        return True
            return False

        return dfs(0)