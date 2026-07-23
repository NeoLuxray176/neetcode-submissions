class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        n, m = len(heights), len(heights[0])

        pacific, atlantic = set(), set()

        def dfs(i, j, ocean, previousHeight):
            if i < 0 or i >= n:
                return
            if j < 0 or j >= m:
                return
            if (i, j) in ocean:
                return
            if heights[i][j] < previousHeight:
                return


            ocean.add((i, j))
            dfs(i + 1, j, ocean, heights[i][j])
            dfs(i - 1, j, ocean, heights[i][j])
            dfs(i, j + 1, ocean, heights[i][j])
            dfs(i, j - 1, ocean, heights[i][j])

        for i in range(m):
            dfs(0, i, pacific, heights[0][i])
            dfs(n - 1, i, atlantic, heights[n - 1][i])

        for j in range(n):
            dfs(j, 0, pacific, heights[j][0])
            dfs(j, m - 1, atlantic, heights[j][m - 1])

        res = []
        for i in range(n):
            for j in range(m):
                if (i, j) in atlantic and (i , j) in pacific:
                    res.append([i , j])

        return res