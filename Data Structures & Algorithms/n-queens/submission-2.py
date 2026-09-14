class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []

        cols = set()
        posdia = set()
        negdia = set()

        board = [["."] * n for _ in range(n)]

        # print(board)

        def backtrack(row : int) -> None:
            if row == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return

            for col in range(n):
                if col in cols:
                    continue
                if col - row in negdia:
                    continue
                if col + row in posdia:
                    continue

                cols.add(col)
                negdia.add(col - row)
                posdia.add(col + row)
                # print(f"[{row}][{col}]")
                board[row][col] = "Q"

                backtrack(row + 1)

                cols.remove(col)
                negdia.remove(col - row)
                posdia.remove(col + row)
                board[row][col] = "."

        backtrack(0)
        return res