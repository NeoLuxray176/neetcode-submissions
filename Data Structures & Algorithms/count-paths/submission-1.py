class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        grid = [[0 for _ in range(n)] for _ in range(m)]

        for j in range(m):
            grid[j][0] = 1
        for i in range(n):
            grid[0][i] = 1

        for i in range(1, m):
            for j in range(1, n):
                a, b = 0, 0
                if i - 1 >= 0:
                    a = grid[i-1][j]
                if j - 1 >= 0:
                    b = grid[i][j-1]
                
                grid[i][j] = a + b

        return grid[m-1][n-1]

        