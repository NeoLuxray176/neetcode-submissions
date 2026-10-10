class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n, m = len(grid), len(grid[0])

        def dfs(i : int, j : int):
            if i < 0 or i >= n:
                return
            if j < 0 or j >= m:
                return

            if grid[i][j] != "1":
                return

            grid[i][j] = "0"

            for x, y in [[0, 1], [1, 0], [-1, 0], [0, -1]]:
                dfs(i + x, j + y)

        res = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1":
                    res += 1
                    dfs(i, j)

        return res
