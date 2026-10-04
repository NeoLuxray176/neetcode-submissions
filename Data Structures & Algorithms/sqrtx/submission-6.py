class Solution:
    def mySqrt(self, x: int) -> int:
        if abs(x) <= 1:
            return x

        prefix = 1
        if x < 0:
            prefix = -1
            x = abs(x)

        res = 2

        while res * res <= x:
            res += 1

        res -= 1

        return prefix * res