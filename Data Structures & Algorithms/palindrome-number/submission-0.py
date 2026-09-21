class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        n = len(x)

        for i in range(n // 2):
            if x[i] != x[n - 1 -i]:
                return False
        return True

