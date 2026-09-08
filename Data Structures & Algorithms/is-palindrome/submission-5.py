class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1

        while left <= right:
            # print(f"{left} {right}")
            if not s[left].isalnum():
                left += 1
                # print(f"A")
                continue
            if not s[right].isalnum():
                right -= 1
                # print(f"B")
                continue
                

            if s[left].lower() == s[right].lower():
                left += 1
                right -= 1
                # print(f"C")
            else:
                return False

        return True
            