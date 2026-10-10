class Solution:
    def checkValidString(self, s: str) -> bool:
        low, high = 0, 0

        for character in s:
            if character == "(":
                low += 1
                high += 1
            elif character == ")":
                low -= 1
                high -= 1
            else:
                low -= 1
                high += 1
            if low < 0:
                low = 0
            if high < 0 or high < low:
                return False

        if low > 0 or high < low:
            return False

        return True