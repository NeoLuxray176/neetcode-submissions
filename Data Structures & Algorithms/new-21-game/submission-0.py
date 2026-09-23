class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        cache = {}

        def dfs(score):
            if score >= k:
                if score <= n:
                    return 1
                else:
                    return 0
            
            if score in cache:
                return cache[score]

            prob = 0
            for i in range(1, maxPts + 1):
                prob += dfs(score + i)

            cache[score] = prob / maxPts
            return cache[score]

        return dfs(0)