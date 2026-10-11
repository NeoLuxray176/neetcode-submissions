class Solution:
    def solve(self, board: List[List[str]]) -> None:
        n, m = len(board), len(board[0])

        stack = []

        for i in range(n):
            stack.append([i, 0])
            stack.append([i, m - 1])
        for j in range(m):
            stack.append([0, j])
            stack.append([n - 1, j])

        while stack:
            i, j = stack.pop()

            if board[i][j] != "O":
                continue

            board[i][j] = "A"

            for x, y in [[0, 1], [1, 0], [-1, 0], [0, -1]]:
                if 0 <= i + x < n and 0 <= j + y < m:
                    stack.append([i, j])

        for i in range(n):
            for j in range(m):
                if board[i][j] == "O":
                    board[i][j] = "X"
                if board[i][j] == "A":
                    board[i][j] = "O"