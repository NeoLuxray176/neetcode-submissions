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
                
                box_r = 3 * (i // 3) + j // 3
                box_c = 3 * (i % 3) + j % 3
                if board[box_r][box_c] != "." and board[box_r][box_c] in square_set:
                    return False
                
                if board[i][j] != ".":
                    row_set.add(board[i][j])
                if board[j][i] != ".":
                    col_set.add(board[j][i])
                if board[box_r][box_c] != ".":
                    square_set.add(board[box_r][box_c])

        return True