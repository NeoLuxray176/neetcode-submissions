class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # Multi source BFS

        n, m = len(grid), len(grid[0])

        visited = set()
        queue = deque()

        def add_cell(i, j):
            if i < 0 or i >= n:
                return
            if j < 0 or j >= m:
                return
            if (i, j) in visited:
                return
            if grid[i][j] == -1 or grid[i][j] == 0:
                return

            visited.add((i, j))
            queue.append([i, j])

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    queue.append([i, j])

        dist = 0
        while queue:
            for _ in range(len(queue)):
                i, j = queue.popleft()
                grid[i][j] = dist

                add_cell(i + 0, j + 1)
                add_cell(i + 1, j + 0)
                add_cell(i + 0, j + -1)
                add_cell(i + -1, j + 0)
            dist += 1
            

