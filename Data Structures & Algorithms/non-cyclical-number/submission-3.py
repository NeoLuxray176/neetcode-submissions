class Solution:
    def isHappy(self, n: int) -> bool:
        
        def get_square(x : int):
            res = 0
            while x:
                res += (x % 10) * (x % 10)
                x = x // 10
            return res

        fast = slow = n

        while fast != 1 and slow != 1:
            fast, slow = get_square(get_square(fast)), get_square(slow)
            if fast != 1 and fast == slow:
                return False

        return True