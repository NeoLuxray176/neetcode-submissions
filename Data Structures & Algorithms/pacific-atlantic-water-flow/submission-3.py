class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        n, m = len(heights), len(heights[0])
        reachable_pacific, reachable_atlantic = set(), set()


        def dfs(i : int, j : int, curr_set : set[int]):
            if 0 > i or i >= n:
                return
            if 0 > j or j >= m:
                return

            curr_set.add((i, j))

            for x, y in [[0, 1], [1, 0], [-1, 0], [0, -1]]:
                if 0 > i + x or i + x >= n:
                    continue
                if 0 > j + y or j + y >= m:
                    continue

                if (i + x, j + y) in curr_set:
                    continue

                if heights[i][j] <= heights[i + x][j + y]:
                    dfs(i + x, j + y, curr_set)

        for i in range(n):
            dfs(i, 0, reachable_pacific)
            dfs(i, m-1, reachable_atlantic)
        for i in range(m):
            dfs(0, i, reachable_pacific)
            dfs(n-1, m - 1 - i, reachable_atlantic)

        res = []
        for i, j in reachable_pacific:
            if (i, j) in reachable_atlantic:
                res.append([i, j])
        
        return res

