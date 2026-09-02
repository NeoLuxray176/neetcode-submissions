class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        # We want to find a path with the smallest large value on it.
        # So we could do some sort of shortest path where the path length is just the maximum value on the path itself. This would mean Dijkstra.

        N = len(grid)
        visit = set()
        minH = [[grid[0][0], 0, 0]]
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        visit.add((0, 0))
        while minH:
            height, row, col = heapq.heappop(minH)
            if row == N -1 and col == N -1:
                return height

            for dr, dc in directions:
                neiR, neiC = row + dr, col + dc

                if(neiR < 0 or neiC < 0 or neiR == N or neiC == N):
                    continue
                if (neiR, neiC) in visit:
                    continue

                visit.add((neiR, neiC))
                heapq.heappush(minH, [max(height, grid[neiR][neiC]), neiR, neiC])

        return -1