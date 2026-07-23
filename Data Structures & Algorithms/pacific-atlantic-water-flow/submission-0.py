class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # We do BFS starting from each of the cells where water can flow in i.e all the 
        # cells at the border.
        # We start with the pacific and store in the output array whether water can flow using
        # a 1.
        # Then do the same with atlantic but store a 3 if we can flow to a cell that
        # contains pacific already and 2 otherwise.
        # Then go through the output and store the indices of all cells that contain a 3

        n, m = len(heights), len(heights[0])

        pacific, atlantic = set(), set()

        def dfs(i, j, visited, previousHeight):
            if i < 0 or i >= n:
                return
            if j < 0 or j >= m:
                return
            if (i, j) in visited:
                return

            if heights[i][j] < previousHeight:
                return

            visited.add((i, j))
            dfs(i + 1, j, visited, heights[i][j])
            dfs(i - 1, j, visited, heights[i][j])
            dfs(i, j + 1, visited, heights[i][j])
            dfs(i, j - 1, visited, heights[i][j])

        for i in range(m):
            dfs(0, i, pacific, heights[0][i])
            dfs(n - 1, i, atlantic, heights[n - 1][i])

        for j in range(n):
            dfs(j, 0, pacific, heights[j][0])
            dfs(j, m - 1, atlantic, heights[j][m - 1])

        res = []
        for i in range(n):
            for j in range(m):
                if (i, j) in atlantic and (i, j) in pacific:
                    res.append([i, j])

        return res
