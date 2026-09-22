class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])
        stack = []

        # Add every border "O" as a starting point.
        for row in range(rows):
            if board[row][0] == "O":
                stack.append((row, 0))
            if board[row][cols - 1] == "O":
                stack.append((row, cols - 1))

        for col in range(cols):
            if board[0][col] == "O":
                stack.append((0, col))
            if board[rows - 1][col] == "O":
                stack.append((rows - 1, col))

        # Mark all "O"s connected to the border as safe.
        while stack:
            row, col = stack.pop()

            if not (0 <= row < rows and 0 <= col < cols):
                continue
            if board[row][col] != "O":
                continue

            board[row][col] = "#"

            stack.append((row + 1, col))
            stack.append((row - 1, col))
            stack.append((row, col + 1))
            stack.append((row, col - 1))

        # Capture surrounded cells and restore safe cells.
        for row in range(rows):
            for col in range(cols):
                if board[row][col] == "O":
                    board[row][col] = "X"
                elif board[row][col] == "#":
                    board[row][col] = "O"