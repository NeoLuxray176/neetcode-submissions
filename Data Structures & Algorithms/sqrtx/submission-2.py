class Solution:
    def mySqrt(self, x: int) -> int:
        for i in range(2, x + 1):
            # print(i, i ** 2, (i + 1) ** 2)
            if i ** 2 == x or (i ** 2 < x and (i + 1) ** 2 > x):
                return i

        return 0