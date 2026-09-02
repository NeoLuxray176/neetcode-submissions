class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # Inputs have no leading zeros, so "0" is the only falsy case.
        # Needed as a guard: otherwise the zero-stripping loop below
        # would consume every digit and return "".
        if "0" in [num1, num2]:
            return "0"

        # An m-digit number times an n-digit number has at most m + n digits.
        res = [0] * (len(num1) + len(num2))

        # Reverse both operands so that index i means "digit of 10^i".
        # res uses the same little-endian convention.
        num1, num2 = num1[::-1], num2[::-1]

        for i1 in range(len(num1)):
            for i2 in range(len(num2)):
                # num1[i1] has place value 10^i1, num2[i2] has 10^i2,
                # so their product belongs at position i1 + i2.
                digit = int(num1[i1]) * int(num2[i2])
                res[i1 + i2] += digit

                # Normalise that position: carry the tens into the next
                # higher position, keep only the ones digit here.
                res[i1 + i2 + 1] += res[i1 + i2] // 10
                res[i1 + i2] = res[i1 + i2] % 10

        # Back to big-endian (most significant digit first).
        res, beg = res[::-1], 0

        # The result may be one digit shorter than m + n, leaving a
        # single leading zero to strip.
        while beg < len(res) and res[beg] == 0:
            beg += 1

        res = map(str, res[beg:])
        return "".join(res)