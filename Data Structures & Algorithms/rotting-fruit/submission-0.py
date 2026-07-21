class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        q = deque()
        fresh = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r, c, 0))   # (cell, distance=0)
                elif grid[r][c] == 1:
                    fresh += 1

        ans = 0
        while q:
            r, c, d = q.popleft()
            for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):
                nr, nc = r+dr, c+dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                    grid[nr][nc] = 2      # mark visited = its distance is d+1
                    fresh -= 1
                    ans = max(ans, d + 1)
                    q.append((nr, nc, d + 1))

        return ans if fresh == 0 else -1