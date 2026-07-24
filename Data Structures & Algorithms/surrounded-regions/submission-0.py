class Solution:
    def solve(self, board: List[List[str]]) -> None:
        n, m = len(board), len(board[0])

        visited = set()

        # Returns True if any of the "O" cells is connected to a border
        # Otherwise we return False
        # If capture is true then we overwrite the board
        def dfs(i : int, j : int):
            if i < 0 or i >= n:
                return
            if j < 0 or j >= m:
                return
            
            if board[i][j] == 'X':
                return

            if (i, j) in visited:
                return

            visited.add((i, j))

            for (x, y) in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                dfs(i + x, j + y)
            return 

        for i in range(n):
            dfs(i, 0)
            dfs(i, m-1)

        for j in range(m):
            dfs(0, j)
            dfs(n - 1, j)

        for i in range(n):
            for j in range(m):
                if (i, j) not in visited:
                    board[i][j] = "X"

        