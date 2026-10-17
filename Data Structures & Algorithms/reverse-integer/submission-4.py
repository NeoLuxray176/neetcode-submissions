class Solution:
    def reverse(self, x: int) -> int:
        res = 0
        is_neg = False

        if x < 0:
            is_neg = True
            x = abs(x)

        while x:
            res = res * 10 + x % 10
            x = x // 10

        if is_neg:
            res *= -1

        if res < -2 ** 31 or res > 2 ** 31 -1:
            return 0

        return res