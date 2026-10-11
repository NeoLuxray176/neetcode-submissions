class Solution:
    def explore(self, n : int, m : int, heights : List[List[int]], reach : List[List[int]], stack : List[int]):
        while stack:
            i, j, height = stack.pop()

            if i < 0 or i >= n or j < 0 or j >= m:
                continue

            if heights[i][j] < height:
                continue
            if reach[i][j]:
                continue

            reach[i][j] = True

            for x, y in [[0, 1], [1, 0], [-1, 0], [0, -1]]:
                stack.append([i + x, j + y, heights[i][j]])

    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # INF = float("inf")
        INF = 0
        n, m = len(heights), len(heights[0])

        reach_pac = [[False] * m for _ in range(n)]
        reach_atl = [[False] * m for _ in range(n)]

        stack = []

        for i in range(n):
            stack.append([i, 0, INF])
            # reach_pac[i][0] = True
        for j in range(m):
            stack.append([0, j, INF])
            # reach_pac[0][j] = True

        self.explore(n, m, heights, reach_pac, stack)

        stack = []

        for i in range(n):
            stack.append([i, m - 1, INF])
            # reach_atl[i][m - 1] = True
        for j in range(m):
            stack.append([n - 1, j, INF])
            # reach_atl[n - 1][j] = True

        self.explore(n, m, heights, reach_atl, stack)

        res = []

        for i in range(n):
            for j in range(m):
                if reach_atl[i][j] and reach_pac[i][j]:
                    res.append([i, j])

        return res
