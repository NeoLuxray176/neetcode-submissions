class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        rev = 0
        curr = x

        while curr:
            rev = rev * 10 + curr % 10
            curr = curr // 10

        return rev == x
        