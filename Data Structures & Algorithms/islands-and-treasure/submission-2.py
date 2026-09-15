class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2147483647
        n, m = len(grid), len(grid[0])

        # Start DFS from each of the treasure chests and fill in the distances
        # Do we need to repeatedly calculate the values of reachable cells?
        # Yes, I'd say so because we cannot know anything about how close the next treasure is without additional computation

        visited = set()
        queue = deque()

        def add_cell(row, col):
            if row < 0 or row >= n:
                return
            if col < 0 or col >= m:
                return
            if grid[row][col] == -1:
                return
            if (row, col) in visited:
                return
            
            visited.add((row, col))
            queue.append([row, col])

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    queue.append([i, j])
                    visited.add((i, j))

        dist = 0
        while queue:
            for i in range(len(queue)):
                j, h = queue.popleft()
                grid[j][h] = dist
                add_cell(j + 0, h + 1)
                add_cell(j + 1, h + 0)
                add_cell(j + 0, h + -1)
                add_cell(j + -1, h + 0)
            dist += 1