class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            row_set = set()
            col_set = set()
            square_set = set()
            for j in range(9):
                if board[i][j] != "." and board[i][j] in row_set:
                    return False
                if board[j][i] != "." and board[j][i] in col_set :
                    return False
                if board[j // 3][j % 3] != "." and board[j // 3][j % 3] in square_set:
                    return False
                
                if board[i][j] != ".":
                    row_set.add(board[i][j])
                if board[j][i] != ".":
                    col_set.add(board[j][i])
                if board[j // 3][j % 3] != ".":
                    square_set.add(board[j // 3][j % 3])

                # 0 1 2 3 4 5 6 7 8 9
                # 0 0 0 1 1 1 2 2 2  
                # 0 1 2 0 1 2 0 1 2

        return True