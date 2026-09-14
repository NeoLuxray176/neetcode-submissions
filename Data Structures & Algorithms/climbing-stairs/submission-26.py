class Solution:
    def climbStairs(self, n: int) -> int:
        if not hasattr(self, "cache"):
            self.cache = {}

        if n < 1:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 2

        if n in self.cache:
            return self.cache[n]

        res = self.climbStairs(n - 1) + self.climbStairs(n - 2)

        self.cache[n] = res

        return res