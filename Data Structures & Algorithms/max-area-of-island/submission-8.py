class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])

        def dfs(i : int, j : int) -> int:
            if i < 0 or i >= n:
                return 0
            if j < 0 or j >= m:
                return 0

            if grid[i][j] != 1:
                return 0

            grid[i][j] = 0

            res = 1
            for x, y in [[0, 1], [1, 0], [-1, 0], [0, -1]]:
                res += dfs(i + x, j + y)

            return res

        res = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    res = max(res, dfs(i, j))

        return res

        