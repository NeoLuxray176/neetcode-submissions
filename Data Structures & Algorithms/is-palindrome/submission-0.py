class Solution:
    def isPalindrome(self, s: str) -> bool:
        n = len(s)
        i = 0
        j = n - 1

        while i < n:
            if not s[i].isalnum():
                i += 1
                continue
            
            if not s[j].isalnum():
                j -= 1
                continue
            
            print(f"{s[i]} {s[j].isalnum()} {s[j]} {s[j].isalnum()}")
            if s[i].lower() != s[j].lower():
                return False
            i += 1
            j -= 1
        
        return True
        