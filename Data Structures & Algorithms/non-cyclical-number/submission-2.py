class Solution:
    def get_next(self, n: int) -> int:
        total = 0
        while n > 0:
            digit = n % 10
            total += digit * digit
            n = n // 10
        return total

    def isHappy(self, n: int) -> bool:
        if n == 1:
            return True
        slow, fast = n, self.get_next(n)

        while slow != fast:
            slow = self.get_next(slow)
            fast = self.get_next(self.get_next(fast))
            if slow == 1:
                return True
        
        return slow == 1