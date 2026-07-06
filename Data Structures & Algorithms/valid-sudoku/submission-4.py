class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board)
        
        rows = defaultdict(set)
        cols = defaultdict(set)
        sqrs = defaultdict(set)

        for i in range(n):
            for j in range(n):
                curr_val = board[i][j]
                if curr_val == ".":
                    continue
                
                if curr_val in rows[i]:
                    return False
                if curr_val in cols[j]:
                    return False
                if curr_val in sqrs[(i//3,j//3)]:
                    return False
                
                rows[i].add(curr_val)
                cols[j].add(curr_val)
                sqrs[(i//3,j//3)].add(curr_val)
        
        return True