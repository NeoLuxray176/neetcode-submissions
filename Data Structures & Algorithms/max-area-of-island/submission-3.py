class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])

        res = 0
        self.curr_island_size = 0

        def dfs(i : int, j : int):
            if i < 0 or i > n - 1:
                return
            if j < 0 or j > m - 1:
                return
            
            if grid[i][j] == 0:
                return

            self.curr_island_size += 1
            grid[i][j] = 0

            for x, y in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
                dfs(i + x, j + y)

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    dfs(i, j)
                res = max(res, self.curr_island_size)
                self.curr_island_size = 0

        return res