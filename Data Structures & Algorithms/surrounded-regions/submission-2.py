class Solution:
    def solve(self, board: List[List[str]]) -> None:
        n, m = len(board), len(board[0])

        def dfs(i : int, j : int):
            if board[i][j] != "O":
                return

            board[i][j] = "#"

            for x, y in [[0, 1], [1, 0], [-1, 0], [0, -1]]:
                if i + x < 0 or i + x >= n:
                    continue
                if j + y < 0 or j + y >= m:
                    continue
                dfs(i + x, j + y)

        for i in range(n):
            dfs(i, 0)
            dfs(i, m - 1)
        for j in range(m):
            dfs(0, j)
            dfs(n - 1, j)
        
        for i in range(n):
            for j in range(m):
                if board[i][j] == "O":
                    board[i][j] = "X"
                if board[i][j] == "#":
                    board[i][j] = "O"