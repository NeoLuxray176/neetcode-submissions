class Solution:
    def get_next(self, n : int) -> int:
        output = 0

        while n:
            digit = n % 10
            digit = digit * digit
            output += digit
            n = n // 10
        
        return output


    def isHappy(self, n: int) -> bool:
        if n == 1:
            return True

        slow, fast = n, self.get_next(n)

        while slow != 1:
            slow = self.get_next(slow)
            fast = self.get_next(self.get_next(fast))

            if slow == 1:
                return True

            if slow == fast:
                return False

        return True



        