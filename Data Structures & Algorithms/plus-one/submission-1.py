class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        carry = 0
        increment = 1

        for i in range(n - 1, -1, -1):
            curr = digits[i] + increment + carry
            carry = 0
            increment = 0

            if curr > 9:
                curr = curr % 10
                carry = 1
            
            digits[i] = curr

        res = digits

        if carry:
            res = [carry] + res

        return res