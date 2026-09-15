class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        n, m = len(grid), len(grid[0])


        def dfs(i : int, j : int):
            if i < 0 or i > n - 1:
                return
            if j < 0 or j > m - 1:
                return

            if grid[i][j] == "1":
                grid[i][j] = "0"
            else:
                return

            directions = [[0, 1], [1, 0], [-1, 0], [0, -1]]

            for x, y in directions:
                dfs(i + x, j + y)

        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1":
                    res += 1
                    dfs(i, j)
        
        return res
