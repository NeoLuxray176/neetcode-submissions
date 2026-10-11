class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        n, m = len(grid), len(grid[0])


        def dfs(i : int, j : int, dist : int):
            if i < 0 or i >= n:
                return
            if j < 0 or j >= m:
                return

            if grid[i][j] == -1:
                return

            if grid[i][j] < dist:
                return

            grid[i][j] = dist

            for x, y in [[0, 1], [1, 0], [-1, 0], [0, -1]]:
                dfs(i + x, j + y, dist + 1)

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    dfs(i, j, 0)

        

