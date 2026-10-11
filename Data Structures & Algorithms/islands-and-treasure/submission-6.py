class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        n, m = len(grid), len(grid[0])

        queue = deque()
        visited = set()

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    queue.append([i, j, 0])

        while queue:
            i, j, dist = queue.popleft()

            if (i, j) in visited:
                continue

            if i < 0 or i >= n:
                continue
            
            if j < 0 or j >= m:
                continue

            if grid[i][j] == -1:
                continue

            grid[i][j] = min(grid[i][j], dist)

            visited.add((i, j))

            for x, y in [[0, 1], [1, 0], [-1, 0], [0, -1]]:
                queue.append([i + x, j + y, dist + 1])