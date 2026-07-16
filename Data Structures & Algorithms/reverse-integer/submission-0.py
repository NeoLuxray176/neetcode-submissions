class Solution:
    def reverse(self, x: int) -> int:
        s = f"{abs(x)}"[::-1]
        i = int(s)

        if x < 0:
            i *= -1

        if i < -2**31:
            return 0
        if i > 2**31 - 1:
            return 0

        return i