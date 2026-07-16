class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)

        carry = 1

        for i in range(n - 1, -1 , -1):
            digits[i] += carry
            carry = 0

            if digits[i] > 9:
                carry = 1
                digits[i] = 0

        if carry > 0:
            digits = [1] + digits

        return digits