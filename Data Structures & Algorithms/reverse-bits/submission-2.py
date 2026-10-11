class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        i = 32

        while i:
            res = res << 1 | n & 1
            n = n >> 1
            i -= 1

        return res