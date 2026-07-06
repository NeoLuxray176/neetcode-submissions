class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = defaultdict(set)
        rows = defaultdict(set)
        squares = defaultdict(set)

        for i in range(9):
            for j in range(9):
                curr_val = board[i][j]
                if curr_val == ".":
                    continue
                
                if curr_val in rows[i]:
                    return False
                if curr_val in cols[j]:
                    return False
                if curr_val in squares[(i // 3, j // 3)]:
                    return False

                rows[i].add(curr_val)
                cols[j].add(curr_val)
                squares[(i // 3, j // 3)].add(curr_val)

        return True