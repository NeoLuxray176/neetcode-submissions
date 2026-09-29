class Solution:
    def isPalindrome(self, s: str) -> bool:
        n = len(s)
        left, right = 0, n - 1

        while left <= right:
            if left < n and not s[left].isalnum():
                left += 1
                continue
            if right >= 0 and right < n and not s[right].isalnum():
                right -= 1
                continue
            
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1

        return True
