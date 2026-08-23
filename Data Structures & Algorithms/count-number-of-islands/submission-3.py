class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid)
        m = len(grid[0]) if n > 0 else 0

        res = 0

        def dfs(i, j):
            if i < 0 or j < 0 or i > n - 1 or j > m - 1:
                return

            if grid[i][j] == "1":
                grid[i][j] = 0
            else:
                return

            dfs(i + 1, j)
            dfs(i - 1, j)

            dfs(i, j + 1)
            dfs(i, j - 1)

        for i in range(n):
            for j in range(m):
                # print(f"Checking {i}{j} {grid[i][j]} {grid[i][j] == 1}")
                if grid[i][j] == "1":
                    print("Increment res!")
                    res += 1
                    dfs(i, j)
        
        return res
