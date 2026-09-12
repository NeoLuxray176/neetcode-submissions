class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n, m = len(board), len(board[0])
        directions = [[0, 1], [1, 0], [-1, 0], [0, -1]]

        def dfs(k : int, i : int, j : int) -> bool:
            if k == len(word):
                return True
            if i < 0 or i >= n:
                return False
            if j < 0 or j >= m:
                return False
            if board[i][j] != word[k]:
                return False

            curr = board[i][j]
            board[i][j] = "#" # track forwards, we are not allowed to reuse this cell

            for a, b in directions:
                if dfs(k + 1, i + a, j + b):
                    return True

            board[i][j] = curr # backtrack
            return False

        for i in range(n):
            for j in range(m):
                if dfs(0, i, j):
                    return True
        return False
