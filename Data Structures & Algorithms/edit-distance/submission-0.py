class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)

        def dfs(i, j):
            # All remaining charactesr in word2 must be inserted
            if i == m:
                return n - j
            # All remaining charactesr in word1 must be inserted
            if j == n:
                return m - i

            # No operation needed, continue
            if word1[i] == word2[j]:
                return dfs(i + 1, j + 1)

            # Consider all three operations. Delete, insert and replace and
            # take the min of all three.
            # Add one for the current operation (whatever it was)
            res = min(dfs(i + 1, j), dfs(i, j + 1))
            res = min(res, dfs(i + 1, j + 1))
            return res + 1

        return dfs(0, 0)