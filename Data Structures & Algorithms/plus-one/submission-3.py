class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        i = n - 1
        carry = 1

        while carry > 0 and i >= 0:
            digits[i] += carry
            carry = 0

            if digits[i] > 9:
                carry = 1
                digits[i] = 0

            i -= 1

        if carry:
            return [1] + digits

        return digits
