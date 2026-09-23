class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n, m = len(board), len(board[0])

        # Rows
        curr = set()
        for i in range(n):
            curr = set()
            for j in range(m):
                if board[i][j] != "." and board[i][j] in curr:
                    # print("rows", i, j)
                    return False
                curr.add(board[i][j])

        # Cols
        curr = set()
        for j in range(m):
            curr = set()
            for i in range(n):    
                if board[i][j] != "." and board[i][j] in curr:
                    # print("cols", i, j)
                    return False
                curr.add(board[i][j])

        for x in [0, 3, 6]:
            for y in [0, 3, 6]:
                curr = set()
                for i in range(x, x + 3):
                    for j in range(y, y + 3):
                        if board[i][j] != "." and board[i][j] in curr:
                            return False
                        curr.add(board[i][j])

        return True