class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        n, m = len(heights), len(heights[0])

        def bfs(starts):
            visited = set(starts)
            stack = list(starts)
            while stack:
                r, c = stack.pop()
                for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    nr, nc = r + dr, c + dc
                    if not (0 <= nr < n and 0 <= nc < m):
                        continue
                    if (nr, nc) in visited:
                        continue
                    if heights[nr][nc] < heights[r][c]:
                        continue
                    visited.add((nr, nc))
                    stack.append((nr, nc))
            return visited

        pacific = bfs([(0, j) for j in range(m)] + [(i, 0) for i in range(n)])
        atlantic = bfs([(n - 1, j) for j in range(m)] + [(i, m - 1) for i in range(n)])

        return [list(cell) for cell in pacific & atlantic]