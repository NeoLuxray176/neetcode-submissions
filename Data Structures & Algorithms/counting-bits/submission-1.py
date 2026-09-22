class Solution:
    def countBits(self, n: int) -> List[int]:
        # dp[i] stores the number of 1-bits in the binary representation of i.
        dp = [0] * (n + 1)

        # Largest power of two that is less than or equal to i.
        offset = 1

        for i in range(1, n + 1):
            # If i is the next power of two, update the offset.
            # Powers of two contain exactly one 1-bit.
            if offset * 2 == i:
                offset = i

            # Remove the largest power of two from i.
            # That power contributes one 1-bit, while the number of 1-bits
            # in the remainder was already calculated earlier.
            #
            # Example: i = 6 (110), offset = 4 (100)
            #          i - offset = 2 (010)
            #          bits(6) = 1 + bits(2)
            dp[i] = 1 + dp[i - offset]

        return dp