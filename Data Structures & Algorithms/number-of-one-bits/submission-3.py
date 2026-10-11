class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0

        while n:
            res += n & 1 # This is one if the last bit of n is one
            n = n >> 1 # Shift right by one discarding the bit we have just processed
            # repeat until n is 0

        return res