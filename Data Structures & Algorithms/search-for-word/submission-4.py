class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n, m = len(board), len(board[0])

        def dfs(i : int, j : int, index : int) -> bool:
            if i < 0 or i >= n:
                return False
            if j < 0 or j >= m:
                return False
            if index >= len(word):
                return True

            if board[i][j] != word[index]:
                return False

            tmp = board[i][j]
            board[i][j] = "#"

            for x, y in [[0, 1], [1, 0], [-1, 0], [0, -1]]:
                if dfs(i + x, j + y, index + 1):
                    return True
            
            board[i][j] = tmp

            return False

        for i in range(n):
            for j in range(m):
                if dfs(i, j, 0):
                    return True

        return False
                    