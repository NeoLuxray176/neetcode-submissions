class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        n, m = len(matrix), len(matrix[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        dp = [[0] * m for _ in range(n)]

        def dfs(row: int, col: int) -> int:
            if dp[row][col] != 0:
                return dp[row][col]

            best = 1
            for dr, dc in directions:
                r, c = row + dr, col + dc
                if 0 <= r < n and 0 <= c < m and matrix[r][c] > matrix[row][col]:
                    best = max(best, 1 + dfs(r, c))

            dp[row][col] = best
            return best

        return max(dfs(row, col) for row in range(n) for col in range(m))