class Solution:
    def reverseBits(self, n: int) -> int:
        # 3. Bit Manipulation (Optimal)
            # Intuition
            # We are given a 32-bit unsigned integer and need to reverse its bits.

            # Instead of reversing bits one-by-one, we can do this much faster by using a classic bit-manipulation trick called bitwise divide and conquer.

            # The key idea is:

            # Reverse bits in large blocks first
            # Then gradually reverse smaller and smaller blocks
            # Until all individual bits are reversed
            # This works because reversing bits is equivalent to:

            # swapping the left half with the right half
            # then swapping bytes
            # then nibbles (4 bits)
            # then pairs
            # finally single bits
            # Each step rearranges bits closer to their final reversed positions.
        res = n
        res = (res >> 16) | (res << 16) & 0xFFFFFFFF
        res = ((res & 0xff00ff00) >> 8) | ((res & 0x00ff00ff) << 8)
        res = ((res & 0xf0f0f0f0) >> 4) | ((res & 0x0f0f0f0f) << 4)
        res = ((res & 0xcccccccc) >> 2) | ((res & 0x33333333) << 2)
        res = ((res & 0xaaaaaaaa) >> 1) | ((res & 0x55555555) << 1)
        return res & 0xFFFFFFFF