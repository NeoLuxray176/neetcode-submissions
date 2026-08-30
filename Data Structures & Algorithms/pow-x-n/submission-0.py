class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0:
            return 0
        if x == 1:
            return 1

        res = 1
        for i in range(abs(n)):
            res *= x

        return res if n >= 0 else 1 / res