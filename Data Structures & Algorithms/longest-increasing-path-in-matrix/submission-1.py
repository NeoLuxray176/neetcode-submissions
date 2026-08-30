class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        n, m = len(matrix), len(matrix[0])  # grid dimensions
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # up, down, left, right
        dp = [[0] * m for _ in range(n)]  # dp[row][col] = longest increasing path starting there; 0 = not yet computed

        def dfs(row: int, col: int) -> int:
            if dp[row][col] != 0:  # already computed this cell, reuse cached result
                return dp[row][col]

            best = 1  # every cell is a path of length 1 on its own
            for dr, dc in directions:  # try all 4 neighbors
                r, c = row + dr, col + dc
                if 0 <= r < n and 0 <= c < m and matrix[r][c] > matrix[row][col]:
                    # neighbor is in bounds AND strictly greater -> valid increasing step
                    best = max(best, 1 + dfs(r, c))  # extend path through that neighbor

            dp[row][col] = best  # cache result before returning
            return best

        # try every cell as a starting point, keep the best path found
        return max(dfs(row, col) for row in range(n) for col in range(m))