class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x

        left, right = 1, x // 2
        ans = 1

        while left <= right:
            middle = (left + right) // 2
            if middle * middle <= x:
                ans = middle
                left = middle + 1
            else:
                right = middle - 1

        return ans