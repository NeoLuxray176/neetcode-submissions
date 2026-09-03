class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        valid_check = [0] * 10

        # Check rows
        for i in range(9):
            valid_check = [0] * 10
            for j in range(9):
                curr = board[i][j]
                if curr != ".":
                    # print(f"curr={curr} {len(valid_check)}")
                    if valid_check[int(curr)] > 0:
                        return False
                    else:
                        valid_check[int(curr)] = 1
                    
        # Check columns
        for i in range(9):
            valid_check = [0] * 10
            for j in range(9):
                if board[j][i] != ".":
                    if valid_check[int(board[j][i])] > 0:
                        return False
                    else:
                        valid_check[int(board[j][i])] = 1

        for a in [0, 3, 6]:
            for b in [0, 3, 6]:
                valid_check = [0] * 10
                for i in range(3):
                    for j in range(3):
                        curr = board[a + i][b + j]
                        if curr != ".":
                            if valid_check[int(curr)] > 0:
                                return False
                            else:
                                valid_check[int(curr)] = 1

        return True