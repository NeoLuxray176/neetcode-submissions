class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n = len(board)
        m = len(board[0])

        found = False

        def backtrack(i : int, x : int, y : int):
            if i == len(word):
                return True

            if (x < 0 or y < 0 or x >= n or y >= m or 
            word[i] != board[x][y] or board[x][y] == "#"):
                return False
            
            board[x][y] = "#"
            res = (backtrack(i+1, x + 1, y)
            or backtrack(i+1, x - 1, y)
            or backtrack(i+1, x, y + 1)
            or backtrack(i+1, x, y - 1))
            board[x][y] = word[i]
            return res

        for i in range(n):
            for j in range(m):
                if backtrack(0, i, j):
                    return True
        return found