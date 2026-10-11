class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # We do multi source BFS and rot the next generation of fruits
        # we keep track of whether new fruit is now rottten and break as soon as this isn't the case anymore
        # 

        n, m = len(grid), len(grid[0])
        queue = deque()
        res = 0

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    queue.append((i, j))

        while queue:
            changed = False
            nextq = []
            for i, j in queue:
                if i < 0 or i >= n:
                    continue
                if j < 0 or j >= m:
                    continue

                if grid[i][j] != 2:
                    continue

                for x, y in [[0, 1], [1, 0], [-1, 0], [0, -1]]:
                    if 0 <= i + x < n and 0 <= j + y < m and grid[i + x][j + y] == 1:
                        changed = True
                        grid[i + x][j + y] = 3
                        nextq.append((i + x, j + y))

            if changed:
                res += 1
            for i in range(n):
                for j in range(m):
                    if grid[i][j] == 3:
                        grid[i][j] = 2

            queue = nextq

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    return -1

        return res