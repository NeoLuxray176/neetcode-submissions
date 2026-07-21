class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0

        n, m = len(grid), len(grid[0])
        # queue = []

        for i in range(n):
            for j in range(m):
                queue = []
                queue.append((i,j))
                curr_island = 0
                # print(f"Checking ({i},{j})")
                while queue:
                    k, l = queue.pop()
                    if k >= 0 and k < n and l >= 0 and l < m:
                        if grid[k][l] == 1:
                            curr_island += 1
                            grid[k][l] = 0
                            queue.append((k + 1, l))
                            queue.append((k - 1, l))
                            queue.append((k, l + 1))
                            queue.append((k, l - 1))
                
                res = max(res, curr_island)

        return res

