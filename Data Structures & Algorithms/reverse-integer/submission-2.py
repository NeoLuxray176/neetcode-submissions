class Solution:
    def reverse(self, x: int) -> int:
        sign = 1
        if x < 0:
            sign = -1
            x = abs(x)
        y = 0

        while x:
            # print(x, y)
            y *= 10
            y += x % 10
            x = x // 10

        if y > 2 ** 31 - 1:
            return 0
        if y < -2 ** 31 - 1:
            return 0

        return y * sign