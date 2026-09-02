from collections import Counter, defaultdict

class CountSquares:
    def __init__(self):
        self.point_count = Counter()       # (x, y) -> how many times added
        self.rows = defaultdict(list)      # y -> list of x's, one entry per add

    def add(self, point: List[int]) -> None:
        x, y = point
        self.point_count[(x, y)] += 1
        self.rows[y].append(x)             # keyed by y, so a row lookup is O(1)

    def count(self, point: List[int]) -> int:
        px, py = point
        total = 0
        for lx in self.rows[py]:           # every stored point sharing the query's row
            side = abs(px - lx)
            if side == 0:                  # the query point itself -> zero area
                continue
            for dy in (side, -side):       # the square can sit above or below the row
                total += (self.point_count[(lx, py + dy)]
                          * self.point_count[(px, py + dy)])
        return total