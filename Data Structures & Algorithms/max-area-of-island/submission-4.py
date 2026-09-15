class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])

        def dfs(i: int, j: int) -> int:
            if i < 0 or i >= n:
                return 0
            if j < 0 or j >= m:
                return 0
            if grid[i][j] == 0:
                return 0

            grid[i][j] = 0
            area = 1

            for x, y in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
                area += dfs(i + x, j + y)

            return area

        res = 0

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    res = max(res, dfs(i, j))

        return res