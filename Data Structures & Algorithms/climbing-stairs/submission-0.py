class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        m = n + 1
        res = [0] * m
        res[1], res[2] = 1, 2

        for i in range(3,m):
            res[i] = res[i-1] + res[i-2]
        
        return res[n]