class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])

        res = 0

        for i in range(n):
            for j in range(m):
                queue = []
                queue.append((i, j))
                curr_island_size = 0

                while queue:
                    k, l = queue.pop()
                    if k < 0 or k > n - 1:
                        continue
                    if l < 0 or l > m - 1:
                        continue
                    
                    if grid[k][l] == 1:
                        curr_island_size += 1
                        grid[k][l] = 0

                        queue.append((k + 0, l + 1))
                        queue.append((k + 1, l + 0))
                        queue.append((k + 0, l + -1))
                        queue.append((k + -1, l + 0))
                
                res = max(res, curr_island_size)
        return res